import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import glob
import re

data_list = glob.glob("dataset/BSDS/images/train/" + "*.jpg")
data_list_num = re.findall(r"\\(\d+).jpg", str(data_list))  # 图片名字
for i in range(len(data_list_num)):
    img = cv.imread("dataset/BSDS/images/train/" + str(data_list_num[i]) + ".jpg")
    row, col, channel = img.shape
    if (row > col):
        img=img.swapaxes(0, 1)
        row, col, channel = img.shape
    img = img[0:row - 1, 0:col - 1,:]

    img2 = np.flip(img, axis=0)
    img3 = np.flip(img, axis=1)
    img4 = np.flip(img2, axis=1)

    cv.imwrite("dataset/BSDS/images/train_flip/" + str(data_list_num[i]) + ".png", img)
    cv.imwrite("dataset/BSDS/images/train_flip/" + str(data_list_num[i]) + "_2" + ".png", img2)
    cv.imwrite("dataset/BSDS/images/train_flip/" + str(data_list_num[i]) + "_3" + ".png", img3)
    cv.imwrite("dataset/BSDS/images/train_flip/" + str(data_list_num[i]) + "_4" + ".png", img4)
