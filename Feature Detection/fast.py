import numpy as np
import cv2
from matplotlib import pyplot as plt

img = plt.imread('1.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img)
img2 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))

# Print all default params
print "Threshold: ", fast.getThreshold()
print "nonmaxSuppression: ", fast.getNonmaxSuppression()
print "neighborhood: ", fast.getType()
print "Total Keypoints with nonmaxSuppression: ", len(kp)

cv2.imwrite('fast_true_1.png',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

print "Total Keypoints without nonmaxSuppression: ", len(kp)

img3 = cv2.drawKeypoints(img, kp, None,color=(255,0,0))

cv2.imwrite('fast_false_1.png',img3)




img = plt.imread('2.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img)
img2 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))

# Print all default params
print "Threshold: ", fast.getThreshold()
print "nonmaxSuppression: ", fast.getNonmaxSuppression()
print "neighborhood: ", fast.getType()
print "Total Keypoints with nonmaxSuppression: ", len(kp)

cv2.imwrite('fast_true_2.png',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img)

print "Total Keypoints without nonmaxSuppression: ", len(kp)

img3 = cv2.drawKeypoints(img, kp, None,color=(255,0,0))

cv2.imwrite('fast_false_2.png',img3)




img = plt.imread('3.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img)
img2 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))

# Print all default params
print "Threshold: ", fast.getThreshold()
print "nonmaxSuppression: ", fast.getNonmaxSuppression()
print "neighborhood: ", fast.getType()
print "Total Keypoints with nonmaxSuppression: ", len(kp)

cv2.imwrite('fast_true_3.png',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img)

print "Total Keypoints without nonmaxSuppression: ", len(kp)

img3 = cv2.drawKeypoints(img, kp, None,color=(255,0,0))

cv2.imwrite('fast_false_3.png',img3)
