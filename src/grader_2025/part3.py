import cv2 as cv
import numpy as np
from utlis import splitBoxes
from utlis import drawGrid
from get_rec import get_rec
from utlis import getTransform
def isMarked(box):
    totalPixels = cv.countNonZero(box)

    if totalPixels > 500:
        return True
    else:
        return False

def sub_get(img):
    width = img.shape[1]
    height = img.shape[0]

    # print (width, height)

    img = img[90:(height - 20), 25:(width - 5)]
    width = img.shape[1]
    height = img.shape[0]

    # print (width, height)

    img = cv.resize(img, (192, 468))

    boxes = splitBoxes(img, 12, 4)
    id = 0
    grid = []
    index = 0
    for i in range(0, 12):
        grid.append([])
        for j in range(0, 4):
            grid[i].append(isMarked(boxes[i * 4 + j]))
            # print(cv.countNonZero(boxes[i * 4 + j]), end=' ')

        # print()
    return grid

def get(img):

    width = img.shape[1]
    height = img.shape[0]

    original = img.copy()
    img = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)[1]
    img = cv.resize(img, (1308, height))

    # print(width, height)
    # cv.imshow('img gets', img)
    # cv.waitKey(0)

    boxes = splitBoxes(img, 1, 6)
    index = 0

    ret = []

    for box in boxes:
        ret.append(sub_get(box))

    return ret

def part3_main(img):

    contours = get_rec(img)
    # img = gray

    tmp = []
    for contour in contours:
        area = cv.contourArea(contour)
        approx = cv.approxPolyDP(contour, 0.02 * cv.arcLength(contour, True), True)
        res = getTransform(img, approx)
        res = res[0:res.shape[0], 0:res.shape[1]]
        tmp.append([res, area])

    tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
    # cv.imshow('img', tmp[0][0])
    tmp = cv.cvtColor(tmp[0][0], cv.COLOR_BGR2GRAY)
    # cv.waitKey(0)
    return get(tmp)