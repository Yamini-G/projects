import numpy as np
import cv2

highThresh	= 0.4
lowThresh		= 0.1
imgFileList	= ('./ip.jpeg', './mypic.jpg')

def sobel (img):
	
	opImgx		= cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
	opImgy		= cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)	
	
	return cv2.bitwise_or(opImgx,opImgy)	

def sketch(frame):	
	
	frame		= cv2.GaussianBlur(frame,(3,3),0)
	invImg	= 255-frame
	edgImg0		= sobel(frame)
	edgImg1		= sobel(invImg)
	edgImg		= cv2.addWeighted(edgImg0,1,edgImg1,1,0)	
	opImg		= 255-edgImg
	return opImg
	
if __name__ == '__main__':
	for imgfile in imgFileList:
		print (imgfile)
		img		= cv2.imread (imgfile,0)
		opImg	= sketch(img)	
		cv2.imshow (imgfile,opImg)
	
	cv2.waitKey()
	cv2.destroyAllWindows()