import cv2
import os
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

def save_landmarks_to_csv(lm_list, label):
    df = pd.DataFrame(lm_list)
    df.to_csv(f"{label}.txt", index=False)

# Đường dẫn đến thư mục chứa video
root_folder = "D:\HAR\Human_acti\ToLearnBlockchain\.venv\HumanActivity"  # Thay bằng đường dẫn thực tế của bạn
labels = ["Clapping", "Meet and Split", "Sitting", "Standing Still",
          "Walking", "Walking While Reading Book", "Walking While Using Phone"]

# Lặp qua từng thư mục và video để xử lý
for label in labels:
    folder_path = os.path.join(root_folder, label)
    for video_file in os.listdir(folder_path):
        video_path = os.path.join(folder_path, video_file)
        print(f"Processing {video_file} for action {label}...")
        lm_list = process_video(video_path, label)
        save_landmarks_to_csv(lm_list, label)
