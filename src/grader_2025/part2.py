
import cv2 as cv
import numpy as np
from utlis import splitBoxes
from utlis import drawGrid
from utlis import getTransform
from get_rec import get_rec

def isMarked(box):
    totalPixels = cv.countNonZero(box)

    if totalPixels > 400:
        return True
    else:
        return False

def get(img, number):

    width = img.shape[1]
    height = img.shape[0]
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.threshold(gray, 170, 255, cv.THRESH_BINARY_INV)[1]

    crop_img = img[85:(height - 20), 45:(width - 5)]

    # print(width, height)

    resized = cv.resize(crop_img, (200, 120))

    # cv.imshow('crop', crop_img)
    # cv.imshow('img', img)
    # cv.imshow('resized', resized)

    questions = 4
    choices = 2

    boxes = splitBoxes(resized, questions, choices)

    # cv.imshow(f"grid 1 number {number}", boxes[0])
    # cv.imshow(f"grid 2 number {number}", boxes[1])

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
                grid[i][j] = grid[i][j][0:h, 6:w]

            # print(i, j)
            # cv.imshow(f'grid {i} {j} {number}', grid[i][j])

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

    # print(ret)
    return ret

def part2_main(img):


    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('img', img)
    # cv.waitKey(0)
    contours = get_rec(img)
    # img = gray

    tmp = []
    for contour in contours:
        area = cv.contourArea(contour)
        approx = cv.approxPolyDP(contour, 0.02 * cv.arcLength(contour, True), True)
        res = getTransform(img, approx)
        res = res[0:res.shape[0], 0:res.shape[1]]
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
        # cv.imshow(f'part 2 {i}', tmp[i][0])
        temp = get(tmp[i][0], i + 1)
        ret.append(temp[0])
        ret.append(temp[1])

    return ret
    # return get(img)