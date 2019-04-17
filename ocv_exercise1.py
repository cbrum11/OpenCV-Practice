import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt

# Functions Used

# cv.imread() - (0, 1, or -1)
    # ...(cv2.IMREAD_COLOR)
    # ...(cv2.IMREAD_GRAYSCALE)
    # ...(cv2.IMREAD_UNCHANGED)
# cv.shape
# cv.imshow()
# cv.namedWindow()
# cv.waitKey()
# cv.destroyAllWindows()

#---------------------------
# Loading and Saving
#---------------------------

# Load a color image in grayscale
img = cv.imread('/Users/csb/Projects/OpenCV-Practice/Example-Images/surly-bike.jpg',cv.IMREAD_GRAYSCALE)
# Show image size (heigh, width, channels (if color))
print(img.shape)
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
# Plotting
# Plotting Styles - https://matplotlib.org/api/pyplot_api.html
#---------------------------

# Plot image
plt.imshow(img,cmap = 'gray', interpolation = 'bicubic')
# Hide X & Y Axis
plt.xticks([]), plt.yticks([])
# Draw Horizontal Line
img_width = img.shape[1]
plt.plot([0,img_width], [100, 100], 'k-', lw=2)
# Show Plot
plt.show()

#---------------------------
# Note on RGB vs. BGR
# --------------------------

# Open CV follows BGR color order
# Matplotlib follows RGB color order
# The conversion can be completed with cv.cvtColor(img, cv2.COLOR_BGR2RGB)