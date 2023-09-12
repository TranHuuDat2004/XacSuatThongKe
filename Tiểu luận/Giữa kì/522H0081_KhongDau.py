import cv2
import numpy as np

# Doc anh tu file
img = cv2.imread('image.jpg')

# Chuyen doi anh sang dang anh xam (grayscale)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Lay kich thuoc cua anh
height, width = img_gray.shape

# Khoi tao mot mang de luu gia tri cua histogram
hist = np.zeros(256)

# Duyet qua tung pixel va dem tan so cua moi gia tri cuong do
for i in range(height):
    for j in range(width):
        hist[img_gray[i,j]] += 1 # tang tan so tuong ung trong mang hist len 1.

# Chuan hoa histogram bang cach chia tung gia tri cho tong so pixel
hist = hist / (height * width)

# Tinh ham phan phoi tich luy (CDF) cua histogram
cdf = np.zeros(256) # Khoi tao mot mang cdf co kich thuoc 256
cdf[0] = hist[0] # Gan gia tri cdf bang gia tri cuong do dau tien trong histogram
for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i] # cho i bang tong cua gia tri cdf cho gia tri (cdf[i-1])

# Nhan CDF voi 255 de co cac gia tri cuong do moi
new_values = np.round(cdf * 255)

# Tao mot mang anh moi voi cac gia tri pixel da can bang
img_eq = np.zeros_like(img_gray) # de luu tru anh da duoc can bang.
for i in range(height):
    for j in range(width):
        img_eq[i,j] = new_values[img_gray[i,j]] # gan gia tri pixel moi cho mang new_values

# Hien thi anh goc va anh da can bang
cv2.imshow('Anh goc', img_gray)
cv2.imshow('Anh da can bang', img_eq)

# Nhan phim bat ky de thoat
cv2.waitKey(0)

# Dong tat ca cua so hien thi
cv2.destroyAllWindows()