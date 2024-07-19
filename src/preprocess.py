import cv2 as cv
import numpy as np
import utlis
import random


def get_frame(img):

    copy = img.copy()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    blur = cv.blur(gray, (3, 3), 1)
    blur = cv.blur(blur, (5, 5), 3)
    _, thresh = cv.threshold(blur, 150, 255, cv.THRESH_BINARY_INV)
    canny = cv.Canny(thresh, 50, 50)

    # cv.imshow('canny', canny)

    contours, _ = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    square = []

    for contour in contours:

        area = cv.contourArea(contour)
        peri = cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, 0.02 * peri, True)

        if (area < 300):
            continue
        if (len(approx) == 4):
            tmpImg = utlis.getTransform(thresh, approx)
            percent = cv.countNonZero(tmpImg) / (tmpImg.shape[0] * tmpImg.shape[1])
            square.append([utlis.Get_Conner_Points(contour), percent])
        # x, y, w, h = cv.boundingRect(approx)


    square = sorted(square, key=lambda x: x[1], reverse=True)

    # square = [0:9]
    square = square[:8]

    original = img.copy()

    def get_area(A, B, C, D):


        A = [(A[0][0][0] + A[1][0][0] + A[2][0][0] + A[3][0][0]) // 4, (A[0][0][1] + A[1][0][1] + A[2][0][1] + A[3][0][1]) // 4]
        B = [(B[0][0][0] + B[1][0][0] + B[2][0][0] + B[3][0][0]) // 4, (B[0][0][1] + B[1][0][1] + B[2][0][1] + B[3][0][1]) // 4]
        C = [(C[0][0][0] + C[1][0][0] + C[2][0][0] + C[3][0][0]) // 4, (C[0][0][1] + C[1][0][1] + C[2][0][1] + C[3][0][1]) // 4]
        D = [(D[0][0][0] + D[1][0][0] + D[2][0][0] + D[3][0][0]) // 4, (D[0][0][1] + D[1][0][1] + D[2][0][1] + D[3][0][1]) // 4]

        res = utlis.reorder2(np.array([A, B, C, D]))
        area = cv.contourArea(res)

        return [res, area]


    res = [[], 0]

    n = len(square)

    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for t in range(k + 1, n):
                    A = square[i][0]
                    B = square[j][0]
                    C = square[k][0]
                    D = square[t][0]

                    # print(i, j, k, t)

                    temp = get_area(A, B, C, D)
                    # print(temp[1])
                    # print(temp[0])
                    if (temp[1] > res[1]):
                        res = temp
                        # print(res[0], res[1])

    reorder = utlis.reorder(res[0])
    imgOutput = utlis.getTransformFix(original, reorder, 1448, 2136)

    return imgOutput
