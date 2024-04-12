import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

for n in range(20000):
    print(n)
    data = cv.imread('E:/dataset/net/random_resize/data/' + str(n) + '.png')
    edge = cv.imread('E:/dataset/net/random_resize/edge/' + str(n) + '.png')

    f = np.random.randint(0, 2)
    if (f == 1):
        cv.imwrite('E:/dataset/net/random_jpg_png_resize/data/' + str(n) + '.jpg', data)
        cv.imwrite('E:/dataset/net/random_jpg_png_resize/edge/' + str(n) + '.png', edge)
    else:
        cv.imwrite('E:/dataset/net/random_jpg_png_resize/data/' + str(n) + '.png', data)
        cv.imwrite('E:/dataset/net/random_jpg_png_resize/edge/' + str(n) + '.png', edge)
