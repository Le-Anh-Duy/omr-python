import get_rec
import cv2 as cv
from grader_2025 import sbd_mdt
from grader_2025 import part1
from grader_2025 import part2
from grader_2025 import part3

img = cv.imread('assets/2025.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)

# resize = cv.resize(img, (500, 500))
# half = cv.resize(img, (0, 0), fx = 0.5, fy = 0.5)


# cv.imshow('Original', half)

# get_rec.get_rec(img)
# get_rec.get_rec(blur)


# print(cv.countNonZero(gray))
# cv.countNonZero(cv.imread('assets/sbd.png'))
# img = cv.imread('assets/sbd2.png')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print("SBD: ", sbd_mdt.student_id(gray))

# img = cv.imread('assets/made2.png')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print("Ma de: ", sbd_mdt.test_id(gray))

img = cv.imread('assets/p3.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


part3.get(gray)
# print(part1.get(gray))

cv.waitKey(0)