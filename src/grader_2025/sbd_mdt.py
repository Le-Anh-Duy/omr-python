# get student id and test id - return a pair of strings

import cv2 as cv
from utlis import drawGrid
from utlis import splitBoxes
from utlis import stackImages


def isMarked(box):
    totalPixels = cv.countNonZero(box)
    if totalPixels > 1000:
        return True
    else:
        return False

def getMarkedAnswer(boxes, questions, choices):
    box_id = 0
    grid = []
    ret_id = []

    for i in range(0, questions):
        grid.append([])
        for j in range(0, choices):
            grid[i].append(box_id)
            box_id += 1

    for j in range(0, choices):
        cur = -1
        for i in range(0, questions):
            if isMarked(boxes[grid[i][j]]):
                if cur == -1:
                    cur = i
                else:
                    cur = -1
                    break

        if cur != -1:
            ret_id.append(str(cur))
        else:
            ret_id.append('?')

    return ''.join(ret_id)

# currently have a rectangle
def student_id(student_rec_img):

    # draw = drawGrid(student_rec_img, 6, 10)
    # cv.imshow('draw', draw)

    choices = 6
    questions = 10

    student_rec_img = cv.resize(student_rec_img, (300, 800))
    threshold = cv.threshold(student_rec_img, 170, 255, cv.THRESH_BINARY_INV)[1]
    boxes = splitBoxes(threshold, questions, choices)
    return getMarkedAnswer(boxes, questions, choices)


def test_id(test_rec_img):
    choices = 3
    questions = 10

    test_rec_img = cv.resize(test_rec_img, (150, 800))
    threshold = cv.threshold(test_rec_img, 170, 255, cv.THRESH_BINARY_INV)[1]
    boxes = splitBoxes(threshold, questions, choices)
    return getMarkedAnswer(boxes, questions, choices)
