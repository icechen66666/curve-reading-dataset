import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


for i in range(5):
    img=cv.imread("dataset/train_mask/"+str(i)+".png")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    row=img.shape[1]  #1600
    col=img.shape[0]  #1200
    background_color=img[0][0]

    for i in range(row-1,0,-1):
        if (img[col//2][i]!=background_color):
            right=i
            break
    for i in range(col-1,0,-1):
        if (img[i][row//2]!=background_color):
            down=i
            break
    for i in range(row):
        if (img[col//3][i]!=background_color):
            left=i
            break
    for i in range(col):
        if (img[i][row//2]!=background_color):
            up=i
            break

    print(left,right,up,down)

    

