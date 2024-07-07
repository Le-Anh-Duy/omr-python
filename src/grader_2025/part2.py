
import cv2 as cv
import numpy as np
from utlis import splitBoxes
from utlis import drawGrid

def isMarked(box):
    totalPixels = cv.countNonZero(box)

    if totalPixels > 250:
        return True
    else:
        return False

def get(img):

    width = img.shape[1]
    height = img.shape[0]

    img = cv.threshold(img, 170, 255, cv.THRESH_BINARY_INV)[1]

    crop_img = img[85:(height - 20), 45:(width - 5)]

    # print(width, height)

    resized = cv.resize(crop_img, (200, 120))

    # cv.imshow('crop', crop_img)
    # cv.imshow('img', img)
    # cv.imshow('resized', resized)

    questions = 4
    choices = 2

    boxes = splitBoxes(resized, questions, choices)

    index = 0

    grid = []

    ret = [[], []]

    for i in range(0, questions):
        grid.append([])
        for j in range(0, choices):
            grid[i].append(boxes[index])
            index += 1



            if j == 0:
                w = grid[i][j].shape[1]
                h = grid[i][j].shape[0]
                grid[i][j] = grid[i][j][0:h, 0:(w - 10)]
            else:
                w = grid[i][j].shape[1]
                h = grid[i][j].shape[0]
                grid[i][j] = grid[i][j][0:h, 10:w]

            print(i, j)
            # cv.imshow(f'grid {i} {j}', grid[i][j])

            TF_box = splitBoxes(grid[i][j], 1, 2)

            # print(i, j, cv.countNonZero(TF_box[0]), cv.countNonZero(TF_box[1]))

            ans = 0
            if isMarked(TF_box[0]):
                ans += 1
            if isMarked(TF_box[1]):
                ans += 2

            op = chr(ord('a') + i)

            if ans == 1:
                ret[j].append({op: 'T'})
            elif ans == 2:
                ret[j].append({op: 'F'})
            else:
                ret[j].append({op: '?'})

    print(ret)
    return ret
