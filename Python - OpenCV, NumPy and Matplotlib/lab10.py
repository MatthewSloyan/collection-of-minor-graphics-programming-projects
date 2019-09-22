import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy
from drawMatches import drawMatches

img = cv2.imread('GMIT1.jpg')
#img = cv2.imread('ExampleImage.jpg')

#convert to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#PART 5,6,7 & 8 
#==================
blockSize = 2
aperture_size = 3
k = 0.04

R = 255
G = 0
B = 51

#deep copy of original image
imgHarris = deepcopy(img)

dst = cv2.cornerHarris(gray_image, blockSize, aperture_size, k)

#loop through image and draw circles on deep copy where corners detected
threshold = 0.05; #number between 0 and 1
for i in range(len(dst)):
	for j in range(len(dst[i])):
		if dst[i][j] > (threshold*dst.max()):
			cv2.circle(imgHarris,(j,i),3,(B, G, R),-1)


#PART 9, 10, 11 & 12 
#===================
maxCorners = 50
qualityLevel = 0.01
minDistance = 10

R = 59
G = 0
B = 255

#deep copy of original image
imgShiTomasi = deepcopy(img)

#set up corners using variables above
corners = cv2.goodFeaturesToTrack(gray_image, maxCorners, qualityLevel, minDistance)

#loop through image and draw circles on deep copy where corners detected
for i in corners:
	x,y = i.ravel()
	cv2.circle(imgShiTomasi,(x,y),3,(B, G, R),-1)
	
	
#PART 9, 10, 11 & 12 
#===================
R = 242
G = 255
B = 0

#deep copy of original image
imgSift = deepcopy(img)

#Initiate SIFT detector with a limit of 50 keypoints 
sift = cv2.SIFT()
kp, des = cv2.SIFT(50).detectAndCompute(gray_image, None) #limit of 50 keypoints

#Draw keypoints
imgSift = cv2.drawKeypoints(imgSift,kp,color=(B, G, R), flags = 4)
	
#Plot all images
#cv2.imshow('Corner Harris',imgHarris)
#cv2.waitKey(0)

#cv2.imshow('Shi Tomasi (GFTT)',imgShiTomasi)
#cv2.waitKey(0)

#cv2.imshow('SIFT',imgSift)
#cv2.waitKey(0)

#cv2.imshow('Original Gray',gray_image)
#cv2.waitKey(0)

#Show all on subplot
nrows = 2
ncols = 2

plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(imgHarris,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Corner Harris'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(cv2.cvtColor(imgShiTomasi,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Shi Tomasi (GFTT)'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,3),plt.imshow(cv2.cvtColor(imgSift,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('SIFT'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,4),plt.imshow(gray_image, cmap = 'gray')
plt.title('Original Gray'), plt.xticks([]), plt.yticks([])

plt.show()

# Advanced Lab ========

#PART 1 ===============

#read in two images to compare
img1 = cv2.imread('GMIT1.jpg', 0)
img2 = cv2.imread('GMIT2.jpg', 0)

# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

#draw matches and display
img3 = drawMatches(img1,kp1,img2,kp2,matches[:20])


#PART 2 ===============

imgNew = cv2.imread('ExampleImage4.jpg')

#convert the image to HSV space
hsv_img = cv2.cvtColor(imgNew, cv2.COLOR_BGR2HSV)

#split the image into each channel (H, S, V)
h, s, v = cv2.split(hsv_img)

#display each channel
nrows = 2
ncols = 2

plt.subplot(nrows, ncols,1),plt.imshow(h, cmap = 'gray')
plt.title('H Channel'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(s, cmap = 'gray')
plt.title('S Channel'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,3),plt.imshow(v, cmap = 'gray')
plt.title('V Channel'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,4),plt.imshow(cv2.cvtColor(hsv_img,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('HSV'), plt.xticks([]), plt.yticks([])

plt.show()
