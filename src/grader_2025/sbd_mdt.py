# get student id and test id - return a pair of strings

import cv2 as cv
from utlis import drawGrid
from utlis import splitBoxes
from utlis import stackImages
from utlis import getTransform
import get_rec

def isMarked(box):
    # cv.destroyAllWindows()
    # cv.imshow('box', box)
    # cv.waitKey(0)

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
            # cv.imshow(f'box {i} {j}', boxes[box_id])
            box_id += 1

    for j in range(0, choices):
        cur = -1
        numPixels = []
        for i in range(0, questions):
            # if isMarked(boxes[grid[i][j]]):
            #     if cur == -1:
            #         cur = i
            #     else:
            #         cur = -1
            #         break
            numPixels.append(cv.countNonZero(boxes[grid[i][j]]))

        maxPixels = max(numPixels)
        id_max = 0
        for i in range(0, questions):
            if numPixels[i] == maxPixels:
                id_max = i
                break

        for i in range(0, questions):
            if i == id_max:
                cur = i
            else:
                if maxPixels - numPixels[i] < 200:
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
    gray = cv.cvtColor(student_rec_img, cv.COLOR_BGR2GRAY)
    blur = cv.blur(gray, (3, 3), 1)
    threshold = cv.threshold(blur, 200, 255, cv.THRESH_BINARY_INV)[1]

    # cv.imshow('student_rec_img bulr', blur)

    boxes = splitBoxes(threshold, questions, choices)


    return getMarkedAnswer(boxes, questions, choices)


def test_id(test_rec_img):
    choices = 3
    questions = 10

    test_rec_img = cv.resize(test_rec_img, (150, 800))
    gray = cv.cvtColor(test_rec_img, cv.COLOR_BGR2GRAY)
    blur = cv.blur(gray, (3, 3), 1)
    threshold = cv.threshold(blur, 200, 255, cv.THRESH_BINARY_INV)[1]
    boxes = splitBoxes(threshold, questions, choices)
    # print("slited")
    return getMarkedAnswer(boxes, questions, choices)



def get_sbd_made(img):

    contours = get_rec.get_rec(img, 180)
    tmp = []
    for contour in contours:
        area = cv.contourArea(contour)
        approx = cv.approxPolyDP(contour, 0.02 * cv.arcLength(contour, True), True)
        res = getTransform(img, approx)

        # cv.imshow('res', res)
        # cv.waitKey(0)
        # print("asfdasdfasdf")
        tmp.append([res, area])



    tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
    tmp = tmp[:2]

    # cv.imshow('tmp 0', tmp[0][0])
    # cv.imshow('tmp 1', tmp[1][0])
    # cv.waitKey(0)


    stu_id = student_id(tmp[0][0])
    made = test_id(tmp[1][0])
    # print(stu_id, test_id)

    return (stu_id, made)