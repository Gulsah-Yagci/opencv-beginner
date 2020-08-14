# Open a image file

# importing opencv library
import cv2

# Read image and assign in a variable
image = cv2.imread("cat.jpg", 0) # if we write 0, this convert image color to grey
"""
* Our image is in same path with python file. So we just need to input name of image.
* imread function: image read. Imread convert image to some numerical array (numpy array).
"""
# print(type(image))

# Showing image another window
cv2.imshow('My cat', image)

# create a new image file
cv2.imwrite('My cat-grey.jpg', image)

# We have to write this so program waits to be closed
cv2.waitKey(0)

# All opencv window close.
cv2.destroyAllWindows()