import get_rec
import cv2 as cv
from grader_2025 import sbd_mdt
from grader_2025 import part1
from grader_2025 import part2
from grader_2025 import part3
from grader_2025 import grade
import preprocess


# img = cv.imread('assets/2025.png')
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
    width = img.shape[1]
    height = img.shape[0]
    info = output[0:700, 1050:width]
    partOne = output[700:1160, 0:width]
    partTwo = output[1160:1470, 0:width]
    partThree = output[1470:height, 0:width]

    p1 = part1.part1_main(partOne)
    # print(p1)
    p1res = grade.part1_grader(p1)
    print(p1res)

    p2 = part2.part2_main(partTwo)
    # print(p2)
    p2res = grade.part2_grader(p2)
    print(p2res)

    p3 = part3.part3_main(partThree)
    # print(p3)
    p3res = grade.part3_grader(p3)
    print(p3res)

    getinfo = sbd_mdt.get_sbd_made(info)
    # print(getinfo)
    jsInfo = grade.get_info(getinfo)
    print(jsInfo)

    # retJson = { grade.get_info(getinfo),
    #     grade.part1_grader(partOne),
    #     grade.part2_grader(partTwo),
    #     grade.part3_grader(partThree)
    # }

    cv.waitKey(0)

grade_2025('assets/sbd-09.png')