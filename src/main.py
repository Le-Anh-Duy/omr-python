import get_rec
import cv2 as cv
from grader_2025 import sbd_mdt
from grader_2025 import part1
from grader_2025 import part2
from grader_2025 import part3
from grader_2025 import grade
import preprocess


# im22g = cv.imread('assets/2025.png')
# cv.imshow('2025', im22g)
# cv.waitKey(0)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)

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

def grade_2025(path):

    img = cv.imread(path)
    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    output = preprocess.get_frame(img)
    width = output.shape[1]
    height = output.shape[0]
    info = output[0:700, 1050:width]
    partOne = output[700:1160, 0:width]
    partTwo = output[1160:1470, 0:width]
    partThree = output[1470:height, 0:width]

    copy = output.copy()
    copy = cv.resize(copy, (0, 0), fx=0.4, fy=0.4)
    # print("output shape: ", output.shape[0], output.shape[1])
    # widthOutput = partThree.shape[1]
    # heightOutput = partThree.shape[0]
    # print(widthOutput, heightOutput)
    # cv.imshow("parthree", partThree)
    # cv.waitKey(0)

    p1 = part1.part1_main(partOne)
    p1res = grade.part1_grader(p1)
    # print(p1)
    print(p1res)

    p2 = part2.part2_main(partTwo)
    p2res = grade.part2_grader(p2)
    # print(p2)
    print(p2res)

    p3 = part3.part3_main(partThree)
    p3res = grade.part3_grader(p3)
    # print(p3)
    print(p3res)

    getinfo = sbd_mdt.get_sbd_made(info)
    jsInfo = grade.get_info(getinfo)
    # print(getinfo)
    print(jsInfo)

    retJson = {jsInfo, p1res, p2res, p3res}

    # cv.waitKey(0)

grade_2025('assets/testA4.png')
