import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

for n in range(10000):
    print(n*2)
    img = cv.imread('E:/dataset/net/net_polyline/random/data/' + str(n) + '.png')
    cv.imwrite('E:/dataset/net/random/data/' + str(n*2) + '.png', img)
    img = cv.imread('E:/dataset/net/net_polyline/random/edge/' + str(n) + '.png')
    cv.imwrite('E:/dataset/net/random/edge/' + str(n * 2) + '.png', img)

    print(n * 2+1)
    img = cv.imread('E:/dataset/net/net_curve/random/data/' + str(n) + '.png')
    cv.imwrite('E:/dataset/net/random/data/' + str(n*2+1) + '.png', img)
    img = cv.imread('E:/dataset/net/net_curve/random/edge/' + str(n) + '.png')
    cv.imwrite('E:/dataset/net/random/edge/' + str(n * 2+1) + '.png', img)
