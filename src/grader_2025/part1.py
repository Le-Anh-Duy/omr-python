
# get the result of part 1 test


import cv2 as cv
import numpy as np
from utlis import splitBoxes
from utlis import drawGrid
from utlis import getTransform
from utlis import stackImages
# import get_rec


def Get_Conner_Points(cont):
    peri = cv.arcLength(cont, True)
    approx = cv.approxPolyDP(cont, 0.02 * peri, True)
    return approx

# return the outter contour list
def get_rec(img):
    # Convert to grayscale
    # cv.imshow('img', img)
    # cv.waitKey(0)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Apply GaussianBlur
    blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
    # blur = gray #cv.blur(gray, (3, 3), 1)

    _, thresh = cv.threshold(blur, 170, 255, cv.THRESH_BINARY_INV)
    # Find contours
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # draw the contours
    # blank = img.copy()
    # cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
    # cv.imshow('Contours', blank)
    # cv.imshow('thresh', thresh)
    # cv.waitKey(0)

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
    new_contours = sorted(new_contours, key=cv.contourArea, reverse=True)
    return new_contours



def isMarked(box):
    totalPixels = cv.countNonZero(box)
    if totalPixels > 500:
        return True
    else:
        return False

def get(img, number):

    questions = 10 # 10 questions
    choices = 4 # 4 choices

    width = img.shape[1]
    height = img.shape[0]
    crop_img = img[40:(height - 15), 40:(width - 2)]

    # print(width, height)
    crop_img = cv.resize(crop_img, (280, 400))

    crop_img = cv.threshold(crop_img, 150, 255, cv.THRESH_BINARY_INV)[1]
    boxes = splitBoxes(crop_img, questions, choices)

    index = 0
    grid = []
    for i in range(0, questions):
        grid.append([])
        for j in range(0, choices):
            grid[i].append(cv.cvtColor(boxes[index], cv.COLOR_BGR2GRAY))
            index += 1

    ret_choices = []

    crop_img = cv.cvtColor(crop_img, cv.COLOR_BGR2GRAY)
    # cv.imshow(f'img {number + 1}', crop_img)
    # print("=================")
    for i in range(0, questions):
        cur = -1
        for j in range(0, choices):
            # cv.imshow(f'box {i + 1} {j + 1} number {number}', grid[i][j])
            # print(cv.countNonZero(grid[i][j]), end=' ')
            if isMarked(grid[i][j]):
                if cur == -1:
                    cur = j
                else:
                    cur = -1
                    break
        if cur != -1:
            ret_choices.append(chr(ord('A') + cur))
        else:
            ret_choices.append('?')
        # print()

    return ret_choices

def part1_main(img):

    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('img', img)
    # cv.waitKey(0)
    contours = get_rec(img)
    # img = gray

    tmp = []
    for contour in contours:
        area = cv.contourArea(contour)
        approx = cv.approxPolyDP(contour, 0.025 * cv.arcLength(contour, True), True)
        res = getTransform(img, approx)



        res = res[0:res.shape[0], 0:res.shape[1] - 5]
        # print(approx)
        mi = 1000000000
        for i in approx:
            mi = min(mi, i[0][0])

        tmp.append([res, area, mi])

    tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
    tmp = tmp[:4]
    tmp = sorted(tmp, key=lambda x: x[2])


    ret = []

    for i in range(0, 4):
        # cv.imshow(f'part1 {i}', tmp[i][0])
        # cv.waitKey(0)
        ret.append(get(tmp[i][0], i))

    return ret
    # return get(img)