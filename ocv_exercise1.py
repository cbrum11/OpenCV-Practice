import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt

# A simple reference for OpenCV functions and Matplotlib

#---------------------------
# Loading/Saving/Data
#---------------------------

# Load a color image in grayscale
img = cv.imread('/Users/csb/Projects/OpenCV-Practice/Example-Images/surly-bike.jpg',cv.IMREAD_COLOR)
# Show image size (heigh, width, channels (if color))
print("Image Size")
print(img.shape)
#S how image data type
print("Image Data Type")
print(img.dtype)
# Show number of pixels
print("Number of Pixels")
print(img.size)
# Give the window a title
cv.imshow("Name of Picture",img)
# Argument is milliseconds.  Waits for keyboard event to move forward.  Can pass a specific key. 0 waits indefinitely
# for keystroke
cv.waitKey(0)
# Exits all windows (must click window).  Can also use cv.destroyWindow() with window name as arg to close specific window.
cv.destroyAllWindows()
# Save an image.
cv.imwrite("test1.jpg",img)

#---------------------------
# Digging In...
#---------------------------

#Find color value at specific pixel location
print("Pixel value @ location 50,100 (row, column)")
print(img[50,100])
#Find color value for an entire row
print("Pixel value of entire row 50 (all columns)")
print(img[50,:])

# Areas of image that match channel appear brighter
# Show red channel/plane
red_img = img[:,:,0]
cv.imshow("Red Picture",red_img)
cv.waitKey(0)
cv.destroyAllWindows()
# Show blue channel/plane
blue_img = img[:,:,1]
cv.imshow("Blue Picture",blue_img)
cv.waitKey(0)
cv.destroyAllWindows()
# Show green channel/plane
green_img = img[:,:,2]
cv.imshow("Green Picture",green_img)
cv.waitKey(0)
cv.destroyAllWindows()

#---------------------------
# Plotting
# Plotting Styles - https://matplotlib.org/api/pyplot_api.html

# Note on RGB vs. BGR
# -------------------

# Open CV follows BGR color order
# Matplotlib follows RGB color order
# The conversion can be completed with cv.cvtColor(img, cv2.COLOR_BGR2RGB)
#---------------------------

# Plot image
#plt.imshow(img,cmap = 'gray', interpolation = 'bicubic')
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img2, interpolation = 'bicubic')
# Hide X & Y Axis
plt.xticks([]), plt.yticks([])
# Draw Horizontal Line
img_width = img.shape[1]
plt.plot([0,img_width], [100, 100], 'k-', lw=2)
# Show Plot
plt.show()

# Plot all row 50 values
plt.plot(img[50,:])
plt.show()

#---------------------------
# Editing an Image
# --------------------------

# Crop the image and display
# Format: img[y:y+h, x:x+h]
# Note: The limits are inclusive (this cropped image would be size 101x101)
cropped_img = img[100:200, 100:200]
cv.imshow("Cropped Image",cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()

