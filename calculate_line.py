import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import interpolate
from scipy.signal import argrelextrema
import pandas as pd
import cv2 as cv


for n in range(3,4):
    print("----------" + str(n) + "----------")
    img_name = str(n)
    img_path = 'dataset/1/train_mask/' + img_name + ".png"
    img = cv.imread(img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, img = cv.threshold(img, 1, 255, cv.THRESH_BINARY)
    col = img.shape[1]
    row = img.shape[0]
    background_color = img[0][0]


    for i in range(0,row):
        if(sum(img[:,i])!=0):
            print(i)
            break

    for i in range(row-1,0,-1):
        if (sum(img[:, i]) != 0):
            print(i)
            break