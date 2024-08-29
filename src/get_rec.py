import cv2 as cv
import cv2
import numpy as np
import utlis
import largestinteriorrectangle as lir


###############################################
# Author: Sahir                               #
# Code:   Detecting Shapes from a Noisy Image #
###############################################

#Import the Libraries
import random


def show_shape(img):

    #Reading the noisy image
    # img = cv2.imread("scanned_document_edge_enhanced.jpg",1)

    #Displaying to see how it looks
    # cv2.imshow("Original",img)

    #Converting the image to Gray Scale
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    #Removing Gaussian Noise
    blur = cv2.GaussianBlur(gray, (3,3),0)

    #Applying inverse binary due to white background and adapting thresholding for better results
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 1)

    #Checking to see how it looks
    # cv2.imshow("Binary",thresh)

    #Finding contours with simple retrieval (no hierarchy) and simple/compressed end points
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #Checking to see how many contours were found
    # print(len(contours))

    #An empty list to store filtered contours
    filtered = []

    #Looping over all found contours
    for c in contours:
        #If it has significant area, add to list
        if cv2.contourArea(c) < 1000:continue
        # cropped_img = img[inner_bb[1]:inner_bb[1] + inner_bb[3], inner_bb[0]:inner_bb[0] + inner_bb[2]]

        # cv2.imshow('Cropped', cropped_img)

        filtered.append(c)

    #Checking the number of filtered contours
    # print(len(filtered))

    #Initialize an equally shaped image
    objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')

    #Looping over filtered contours
    for c in filtered:
        #Select a random color to draw the contour
        col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        #Draw the contour on the image with above color
        cv2.drawContours(objects,[c], -1, col, -1)
        #Fetch contour area
        area = cv2.contourArea(c)
        #Fetch the perimeter
        p = cv2.arcLength(c,True)
        # print(area,p)

    #Finally show the processed image
    # cv2.imshow("Contours",objects)

    # #Closing protocol
    # cv2.waitKey(0)

    return objects

def Get_Conner_Points(cont):
    peri = cv.arcLength(cont, True)
    approx = cv.approxPolyDP(cont, 0.02 * peri, True)
    return approx

# return the outter contour list
def get_rec(img, thresholdValue=150):
    # show_shape(img)
    #Converting the image to Gray Scale
    gray = cv2.cvtColor(show_shape(img),cv2.COLOR_RGB2GRAY)

    kernel = np.ones((5,5),np.uint8)
    erosion = cv.erode(gray,kernel,iterations = 1)

    #Removing Gaussian Noise

    #Applying inverse binary due to white background and adapting thresholding for better results
    thresh = cv2.adaptiveThreshold(erosion, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 205, 1)

    #Checking to see how it looks
    # cv2.imshow("Binary",thresh)
    # cv2.waitKey(0)
    #Finding contours with simple retrieval (no hierarchy) and simple/compressed end points
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    new_contours = []

    for i in range(0, len(contours)):
        area = cv.contourArea(contours[i])
        # check if it is a rectangle
        peri = cv.arcLength(contours[i], True)
        approx = cv.approxPolyDP(contours[i], 0.02 * peri, True)

        if len(approx) == 4 and area > 1000:
            new_contours.append(contours[i])

    new_contours_img = img.copy()
    cv.drawContours(new_contours_img, new_contours, -1, (0, 255, 0), 3)

    height, width, _ = new_contours_img.shape
    resized = cv.resize(new_contours_img, (width // 2, height // 2))

    # cv.imshow('New Contours', resized)
    # cv.waitKey(0)

    # cv.imshow('New Contours', resized)
    # cnt = contours[ci]
    # # Get the bounding rectangle
    # x, y, w, h = cv.boundingRect(cnt)
    # return x, y, w, h

    contour_point = img.copy()
    cnt = 0

    new_contours = sorted(new_contours, key=cv.contourArea, reverse=True)

    for i in new_contours:
        approx = Get_Conner_Points(i)
        cv.drawContours(contour_point, approx, -1, (255, 0, 0), 10)

        tmp = utlis.getTransform(img, approx)
        # newArr.append(tmp)
        # if (cnt == 7):
        # cv.imshow(f'Transformed {cnt}', tmp)
        cnt += 1

    # wind = utlis.stackImages(newArr)
    # cv.imshow('Transformed', wind)
    # contour_point = cv.resize(contour_point, (width // 2, height // 2))
    # cv.imshow('Contour Points', contour_point)

    # cv.waitKey(0)

    return new_contours
