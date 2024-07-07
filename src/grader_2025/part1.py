
# get the result of part 1 test


import cv2 as cv
import numpy as np
from utlis import splitBoxes
from utlis import drawGrid
from utlis import stackImages

def isMarked(box):
    totalPixels = cv.countNonZero(box)
    if totalPixels > 200:
        return True
    else:
        return False

def get(img):

    questions = 10 # 10 questions
    choices = 4 # 4 choices

    width = img.shape[1]
    height = img.shape[0]
    crop_img = img[40:(height - 15), 40:(width - 2)]

    print(width, height)
    # cv.imshow('crop', crop_img)

    # img = cv.resize(img, (300, 800))

    crop_img = cv.resize(crop_img, (280, 400))

    crop_img = cv.threshold(crop_img, 170, 255, cv.THRESH_BINARY_INV)[1]
    cv.imshow('crop', crop_img)

    boxes = splitBoxes(crop_img, questions, choices)
    # tmp = drawGrid(img, choices, questions)
    # cv.imshow('grid', tmp)

    index = 0
    grid = []
    for i in range(0, questions):
        grid.append([])
        for j in range(0, choices):
            grid[i].append(boxes[index])
            index += 1

    ret_choices = []

    for i in range(0, questions):
        cur = -1
        for j in range(0, choices):
            print(i, j, cv.countNonZero(grid[i][j]))
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

    return ret_choices