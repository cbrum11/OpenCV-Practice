import numpy
import cv2

# Functions Used

# cv2.imread() - (0, 1, or -1)
    # cv2.IMREAD_COLOR()
    # cv2.IMREAD_GRAYSCALE()
    # cv2.IMREAD_UNCHANGED()
# cv2.imshow()
# cv2.namedWindow()
# cv2.waitKey()
# cv2.destroyAllWindows()

#Load a color image in grayscale
img = cv2.imread('/Users/csb/Projects/OpenCV-Practice/Example-Images/surly-bike.jpg',1)
cv2.imshow("Name of Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()