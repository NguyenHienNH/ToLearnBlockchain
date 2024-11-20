import os
import cv2
import numpy as np
import mediapipe as mp
import pandas as pd

# Khởi tạo MediaPipe Pose
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

def make_landmark_timestep(results):
    c_lm = []
    for id, lm in enumerate(results.pose_landmarks.landmark):
        c_lm.append(lm.x)
        c_lm.append(lm.y)
        c_lm.append(lm.z)
        c_lm.append(lm.visibility)
    return c_lm

def process_video(video_path, label):
    lm_list = []
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frameRGB)
            if results.pose_landmarks:
                lm = make_landmark_timestep(results)
                lm_list.append(lm)
        else:
            break
    cap.release()
    return lm_list

def save_landmarks_to_csv(lm_list, label, video_name):
    df = pd.DataFrame(lm_list)
    output_folder = os.path.join("D:\\HAR\\Landmarks", label)  # Đường dẫn đến thư mục lưu kết quả
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, f"{video_name}.txt")
    df.to_csv(output_path, index=False)
    print(f"Saved landmarks for {video_name} in action {label}.")

# Đường dẫn đến thư mục chứa video
root_folder = "D:\\HAR\\Data\\organized_labels"  # Thay bằng đường dẫn thực tế của bạn

# Danh sách nhãn hành động với 60 nhãn
labels = [
    'drink', 'eat', 'brush_teeth', 'brush_hair', 'drop', 'pickup', 'throw', 'sit_down',
    'stand_up', 'clap', 'reading', 'writing', 'tear_up_paper', 'wear_jacket', 'take_off_jacket',
    'wear_shoe', 'take_off_shoe', 'wear_glasses', 'take_off_glasses', 'put_on_hat', 'take_off_hat',
    'cheer_up', 'salute', 'kick', 'taking_object_out_of_pocket', 'hopping_one_foot', 'jump_up',
    'make_a_phone_call', 'play_with_phone', 'typing_on_a_keyboard', 'pointing_to_something',
    'taking_a_selfie', 'check_time', 'rub_two_hands', 'nod_head', 'shake_head', 'wipe_face', 'salutes',
    'put_palms_together', 'cross_hands_in_front', 'sneeze', 'staggering', 'falling_down', 'headache',
    'chest_pain', 'back_pain', 'neck_pain', 'nausea', 'fan_self', 'punching', 'kicking', 'pushing',
    'pat_on_back', 'point_finger', 'hugging', 'giving_something', 'touch_pocket', 'handshaking',
    'walking_towards', 'walking_apart'
]

# Xử lý từng video trong từng thư mục nhãn
for label in labels:
    folder_path = os.path.join(root_folder, label)
    for video_file in os.listdir(folder_path):
        video_path = os.path.join(folder_path, video_file)
        print(f"Processing {video_file} for action {label}...")
        lm_list = process_video(video_path, label)
        save_landmarks_to_csv(lm_list, label, os.path.splitext(video_file)[0])
