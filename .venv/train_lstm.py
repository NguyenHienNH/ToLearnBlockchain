import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split

# Danh sách các nhãn hành động và tệp tương ứng
labels = {
    "Clapping": 0,
    "meet_and_split": 1,
    "Sitting": 2,
    "standing_still": 3,
    "Walking": 4,
    "reading_book": 5,
    "using_phone": 6
}

# Thời gian bước
no_of_timesteps = 10
X = []
y = []


# Hàm đọc dữ liệu từ file txt và tạo dữ liệu cho mô hình
def create_dataset_from_file(file_path, label):
    dataset = pd.read_csv(file_path).values  # Đọc file txt
    n_sample = len(dataset)

    # Duyệt qua từng tập dữ liệu với bước thời gian
    for i in range(no_of_timesteps, n_sample):
        X.append(dataset[i - no_of_timesteps:i, :])  # Lưu chuỗi landmarks
        y.append(label)  # Lưu nhãn tương ứng


# Đọc dữ liệu từ từng file txt và tạo tập dữ liệu huấn luyện
for label, label_id in labels.items():
    file_path = f"{label}.txt"  # Đường dẫn đến tệp txt của từng hành động
    create_dataset_from_file(file_path, label_id)

# Chuyển đổi danh sách thành mảng numpy
X, y = np.array(X), np.array(y)
print(f"Shape of X: {X.shape}, Shape of y: {y.shape}")

# Chia tập dữ liệu thành tập train và test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình LSTM
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=len(labels), activation="softmax"))  # Đầu ra softmax cho các lớp

# Compile mô hình
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Huấn luyện mô hình
history = model.fit(X_train, y_train, epochs=16, batch_size=32, validation_data=(X_test, y_test))

# Lưu mô hình đã huấn luyện
model.save("action_recognition_model.h5")
