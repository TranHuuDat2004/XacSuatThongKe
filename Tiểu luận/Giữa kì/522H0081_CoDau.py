import cv2
import numpy as np

# Đọc ảnh từ file
img = cv2.imread('image.jpg')

# Chuyển đổi ảnh sang dạng ảnh xám (grayscale)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Lấy kích thước của ảnh
height, width = img_gray.shape

# Khởi tạo một mảng để lưu giá trị của histogram
hist = np.zeros(256)

# Duyệt qua từng pixel và đếm tần số của mỗi giá trị cường độ
for i in range(height):
    for j in range(width):
        hist[img_gray[i,j]] += 1 # tăng tần số tương ứng trong mảng hist lên 1.

# Chuẩn hóa histogram bằng cách chia từng giá trị cho tổng số pixel
hist = hist / (height * width)

# Tính hàm phân phối tích lũy (CDF) của histogram
cdf = np.zeros(256) # Khởi tạo một mảng cdf có kích thước 256
cdf[0] = hist[0] # Gán giá trị cdf bằng giá trị cường độ đầu tiên trong histogram
for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i]  # cho i bằng tổng của giá trị cdf cho giá trị (cdf[i-1])

# Nhân CDF với 255 để có các giá trị cường độ mới
new_values = np.round(cdf * 255)

# Tạo một mảng ảnh mới với các giá trị pixel đã cân bằng
img_eq = np.zeros_like(img_gray) # để lưu trữ ảnh đã được cân bằng.
for i in range(height):
    for j in range(width):
        img_eq[i,j] = new_values[img_gray[i,j]] # gán giá trị pixel mới cho mảng new_values

# Hiển thị ảnh gốc và ảnh đã cân bằng
cv2.imshow('Ảnh gốc', img_gray)
cv2.imshow('Ảnh đã cân bằng', img_eq)

# Chờ nhấn phím bất kỳ để thoát
cv2.waitKey(0)

# Đóng tất cả cửa sổ hiển thị
cv2.destroyAllWindows() 