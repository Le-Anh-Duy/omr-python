import cv2 as cv
import numpy as np
from utlis import splitBoxes
from utlis import drawGrid

def isMarked(box):
    totalPixels = cv.countNonZero(box)

    if totalPixels > 400:
        return True
    else:
        return False

def sub_get(img):
    width = img.shape[1]
    height = img.shape[0]

    print (width, height)

    img = img[90:(height - 20), 25:(width - 5)]
    width = img.shape[1]
    height = img.shape[0]

    print (width, height)

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

    img = cv.threshold(img, 170, 255, cv.THRESH_BINARY_INV)[1]
    img = cv.resize(img, (1308, height))

    print(width, height)
    cv.imshow('img', img)

    boxes = splitBoxes(img, 1, 6)
    index = 0

    ret = []

    for box in boxes:
        ret.append(sub_get(box))

    return ret
