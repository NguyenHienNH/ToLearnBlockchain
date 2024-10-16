import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import os
import threading
from itertools import islice  # Dùng để lấy giới hạn số video

# Khởi tạo MediaPipe Pose
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# Tải mô hình đã huấn luyện
model = tf.keras.models.load_model("action_recognition_model.h5")

# Danh sách các nhãn hành động tương ứng với mô hình đã huấn luyện
labels = ["Clapping", "meet_and_split", "Sitting", "standing_still",
          "Walking", "reading_book", "using_phone"]

# Bước thời gian
n_time_steps = 10
lm_list = []  # Danh sách landmarks tạm thời

label = "Warmup...."  # Nhãn khởi đầu
warmup_frames = 20  # Số khung hình warmup


def make_landmark_timestep(results):
    c_lm = []
    for lm in results.pose_landmarks.landmark:
        c_lm.append(lm.x)
        c_lm.append(lm.y)
        c_lm.append(lm.z)
        c_lm.append(lm.visibility)
    return c_lm


def draw_landmark_on_image(mpDraw, results, img):
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    for id, lm in enumerate(results.pose_landmarks.landmark):
        h, w, c = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    return img


def draw_class_on_image(label, img):
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 30)
    fontScale = 1
    fontColor = (0, 255, 0)
    thickness = 2
    lineType = 2
    cv2.putText(img, label,
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                thickness,
                lineType)
    return img


# Hàm phát hiện hành động từ danh sách landmarks
def detect(model, lm_list):
    global label
    lm_list = np.array(lm_list)
    lm_list = np.expand_dims(lm_list, axis=0)  # Thêm chiều mới cho mô hình dự đoán
    print(f"Shape for prediction: {lm_list.shape}")
    results = model.predict(lm_list)  # Dự đoán từ mô hình
    print(f"Prediction result: {results}")

    # Lấy nhãn từ kết quả dự đoán
    predicted_label = np.argmax(results, axis=1)[0]
    label = labels[predicted_label]  # Nhãn hành động tương ứng
    return label


# Hàm suy luận trên một video
def inference_on_video(video_path):
    global lm_list, label

    cap = cv2.VideoCapture(video_path)
    i = 0

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)

        i += 1
        if i > warmup_frames:  # Sau khi warmup đủ số khung hình
            print("Start detect....")

            if results.pose_landmarks:
                c_lm = make_landmark_timestep(results)

                lm_list.append(c_lm)
                if len(lm_list) == n_time_steps:
                    # Thực hiện dự đoán khi có đủ số khung hình
                    t1 = threading.Thread(target=detect, args=(model, lm_list,))
                    t1.start()
                    lm_list = []  # Xóa danh sách landmarks sau khi dự đoán

                # Vẽ khung xương lên ảnh
                img = draw_landmark_on_image(mpDraw, results, img)

        # Hiển thị nhãn hành động lên ảnh
        img = draw_class_on_image(label, img)
        cv2.imshow("Inference", img)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Đường dẫn đến thư mục chứa video
root_folder = "D:\HAR\Human_acti\ToLearnBlockchain\.venv\HumanActivity"  # Thay bằng đường dẫn thực tế của bạn

# Lặp qua từng thư mục và video để suy luận, chỉ lấy 7 video đầu tiên
for label_folder in labels:
    folder_path = os.path.join(root_folder, label_folder)
    video_files = os.listdir(folder_path)

    # Chỉ lấy 7 video đầu tiên
    for video_file in islice(video_files, 7):
        video_path = os.path.join(folder_path, video_file)
        print(f"Running inference on {video_file} for action {label_folder}...")
        inference_on_video(video_path)
