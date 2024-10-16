import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import threading

# Khởi tạo MediaPipe Pose
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# Load mô hình LSTM đã huấn luyện
model = tf.keras.models.load_model("action_recognition_model.h5")

# Nhãn của các hành động tương ứng với mô hình đã huấn luyện
labels = {
    0: "Clapping",
    1: "meet_and_split",
    2: "Sitting",
    3: "standing_still",
    4: "Walking",
    5: "reading_book",
    6: "using_phone"
}

# Biến toàn cục
n_time_steps = 10
lm_list = []
label = "Detecting..."


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
    for lm in results.pose_landmarks.landmark:
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
    cv2.putText(img, label, bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
    return img


def detect_action(model, lm_list):
    global label
    lm_list = np.array(lm_list)
    lm_list = np.expand_dims(lm_list, axis=0)
    predictions = model.predict(lm_list)
    predicted_label = np.argmax(predictions)  # Lấy nhãn với giá trị xác suất cao nhất
    label = labels[predicted_label]  # Lấy nhãn từ dict labels
    print(f"Predicted action: {label}")
    return label


# Khởi động camera
cap = cv2.VideoCapture(0)

i = 0
warmup_frames = 60  # Số khung hình để khởi động camera

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    # Khởi động camera và bỏ qua số khung hình đầu tiên
    i += 1
    if i > warmup_frames:
        if results.pose_landmarks:
            # Thu thập landmarks và thêm vào danh sách
            lm = make_landmark_timestep(results)
            lm_list.append(lm)

            # Nếu đã có đủ số lượng khung hình (n_time_steps), tiến hành nhận diện
            if len(lm_list) == n_time_steps:
                # Sử dụng mô hình để dự đoán
                threading.Thread(target=detect_action, args=(model, lm_list,)).start()
                lm_list = []  # Reset danh sách landmarks sau mỗi lần dự đoán

            # Vẽ skeleton lên ảnh
            img = draw_landmark_on_image(mpDraw, results, img)

    # Hiển thị nhãn của hành động trên ảnh
    img = draw_class_on_image(label, img)

    # Hiển thị ảnh
    cv2.imshow("Human Action Recognition", img)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
