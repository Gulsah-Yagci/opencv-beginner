# importing opencv library
import cv2

# Open a image file

image = cv2.imread("cat.jpg")
"""
* Our image is in same path with python file. So we just need to input name of image.
* imread function: image read. Imread convert image to some numerical array.
"""
# print(type(image))

cv2.imshow('My cat',image)

# We have to write this so program kapatılmasın.
cv2.waitKey(0)

# All opencv window close.
cv2.destroyAllWindows()