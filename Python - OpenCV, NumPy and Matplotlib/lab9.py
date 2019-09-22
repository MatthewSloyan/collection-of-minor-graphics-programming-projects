import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('GMIT.jpg',)

#convert to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#write to new file
cv2.imwrite('GMIT_gray.jpg',gray_image)

#cv2.imshow('image',img)
#cv2.waitKey(0)

# Part 6
#======================
nrows = 2
ncols = 1

#plot first two for Part 6
plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.show()

#Part 7
#======================
KernelSizeWidth = 13
KernelSizeHeight = 13

#add a GaussianBlur to image
imgOut = cv2.GaussianBlur(img,(KernelSizeWidth, KernelSizeHeight),0)
#cv2.imwrite('GMIT_blur.jpg',imgOut)

#cv2.imshow('image',imgOut)
#cv2.waitKey(0)

#Part 8
#======================
nrows = 2
ncols = 2

imgOrig = cv2.imread('GMIT.jpg',)

#plot four images for Part 8
plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(imgOrig,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,3),plt.imshow(cv2.GaussianBlur(gray_image,(3, 3),0), cmap = 'gray')
plt.title('3 x 3 Blur'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,4),plt.imshow(cv2.GaussianBlur(gray_image,(13, 13),0), cmap = 'gray')
plt.title('13 x 13 Blur'), plt.xticks([]), plt.yticks([])

plt.show()

#Part 9, 10, 11 & 12
#======================
nrows = 3
ncols = 3

#read in and blur gray image
imgIn = cv2.imread('image_test.jpg',)
gray_test_image = cv2.cvtColor(imgIn, cv2.COLOR_BGR2GRAY)
blurredImg = cv2.GaussianBlur(gray_test_image,(13, 13),0)

#get Horizontal and Vertical sobel image
sobelHorizontal = cv2.Sobel(blurredImg,cv2.CV_64F,1,0,ksize=5) # x dir
sobelVertical = cv2.Sobel(blurredImg,cv2.CV_64F,0,1,ksize=5) # y dir

#combine both H & V Sobel image
sobelCombined = sobelHorizontal + sobelVertical

#apply canny to combined image with a threshold
canny = cv2.Canny(blurredImg,20,50)

#plot all six images
plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(imgIn,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(gray_test_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,3),plt.imshow(sobelHorizontal, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,4),plt.imshow(sobelVertical, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,5),plt.imshow(sobelCombined, cmap = 'gray')
plt.title('Sobel Combined'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,6),plt.imshow(canny, cmap = 'gray')
plt.title('Canny Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

#Advanced Part 1
#======================
threshold = 10

#Loop through sobel combined image and set the value to either 1/0 depending if it's above/below the threshold
for x in sobelCombined:
	if x.all() > threshold:
		x = 1
	else:
		x = 0
	
cv2.imshow('SobelCombined Edited',sobelCombined)
cv2.waitKey(0)


