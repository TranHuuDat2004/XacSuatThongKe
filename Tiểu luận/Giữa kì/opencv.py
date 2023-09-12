# Import the OpenCV library
import cv2

# Read the image file
img = cv2.imread('image.jpg')

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
img_eq = cv2.equalizeHist(img_gray)

# Display the original and equalized images
cv2.imshow('Original image', img_gray)
cv2.imshow('Equalized image', img_eq)

# Wait for a key press to exit
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
