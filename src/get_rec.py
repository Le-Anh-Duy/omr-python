import cv2 as cv
import numpy as np
import utlis

def Get_Conner_Points(cont):
    peri = cv.arcLength(cont, True)
    approx = cv.approxPolyDP(cont, 0.02 * peri, True)
    return approx

# return the outter contour list
def get_rec(img):
    # Convert to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Apply GaussianBlur
    blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
    # blur = gray #cv.blur(gray, (3, 3), 1)

    _, thresh = cv.threshold(blur, 175, 255, cv.THRESH_BINARY_INV)
    # Find contours
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # Get the largest contour

    # draw the contours
    # blank = img.copy()
    # cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
    # cv.imshow('Contours', blank)
    # cv.imshow('original', img)
    # cv.imshow('canny', canny)
    # cv.imshow('gray', gray)
    # cv.imshow('thresh', thresh)
    # cv.imshow('blur', blur)
    # max_area = 0
    # cv.waitKey(0)

    new_contours = []

    for i in range(0, len(contours)):
        area = cv.contourArea(contours[i])
        # check if it is a rectangle
        peri = cv.arcLength(contours[i], True)
        approx = cv.approxPolyDP(contours[i], 0.02 * peri, True)

        if len(approx) == 4 and area > 1000:
            # print(approx)
            new_contours.append(contours[i])

    new_contours_img = img.copy()
    cv.drawContours(new_contours_img, new_contours, -1, (0, 255, 0), 3)

    height, width, _ = new_contours_img.shape
    resized = cv.resize(new_contours_img, (width // 2, height // 2))

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
    contour_point = cv.resize(contour_point, (width // 2, height // 2))
    # cv.imshow('Contour Points', contour_point)

    # cv.waitKey(0)

    return new_contours
