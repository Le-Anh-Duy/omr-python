import get_rec
import cv2 as cv
from grader_2025 import sbd_mdt
from grader_2025 import part1
from grader_2025 import part2
from grader_2025 import part3
from grader_2025 import grade
import preprocess

# return 4 json strings
# 1. info
# 2. part 1
# 3. part 2
# 4. part 3
def grade_2025(path):

    img = cv.imread(path)

    # resize the image to match the size of 1448, 2136
    output = preprocess.get_frame(img)
    width = output.shape[1]
    height = output.shape[0]
    info = output[0:700, 1050:width]
    partOne = output[700:1160, 0:width]
    partTwo = output[1160:1470, 0:width]
    partThree = output[1470:height, 0:width]


    p1 = part1.part1_main(partOne)
    p1res = grade.part1_grader(p1)

    p2 = part2.part2_main(partTwo)
    p2res = grade.part2_grader(p2)

    p3 = part3.part3_main(partThree)
    p3res = grade.part3_grader(p3)

    getinfo = sbd_mdt.get_sbd_made(info)
    jsInfo = grade.get_info(getinfo)

    retJson = [jsInfo, p1res, p2res, p3res]
    return retJson

print(grade_2025('assets/testA4.png'))
