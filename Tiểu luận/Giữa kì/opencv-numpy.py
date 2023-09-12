# Import the OpenCV and NumPy libraries
import cv2
import numpy as np

# Read the image file
img = cv2.imread('image.jpg')

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Get the dimensions of the image
height, width = img_gray.shape

# Initialize an array to store the histogram values
hist = np.zeros(256)

# Loop through each pixel and count the frequency of each intensity value
for i in range(height):
    for j in range(width):
        hist[img_gray[i,j]] += 1

# Normalize the histogram by dividing each value by the total number of pixels
hist = hist / (height * width)

# Compute the cumulative distribution function (CDF) of the histogram
cdf = np.zeros(256)
cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i]

# Multiply the CDF by 255 to get the new intensity values
new_values = np.round(cdf * 255)

# Create a new image array with the equalized pixel values
img_eq = np.zeros_like(img_gray)
for i in range(height):
    for j in range(width):
        img_eq[i,j] = new_values[img_gray[i,j]]

# Display the original and equalized images
cv2.imshow('Original image', img_gray)
cv2.imshow('Equalized image', img_eq)

# Wait for a key press to exit
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
