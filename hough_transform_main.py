import cv2
from houghTransform import *
if __name__ == '__main__':
    imgpath = 'n.png'
    img = cv2.imread(imgpath)
    HoughTransform(img)
