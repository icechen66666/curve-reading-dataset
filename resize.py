import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

for n in range(20000):
    data = cv.imread('E:/dataset/net/random/data/' + str(n) + '.png')
    edge = cv.imread('E:/dataset/net/random/edge/' + str(n) + '.png')

    f = np.random.randint(1, 5)
    print(n, f)
    if (f == 1):
        cv.imwrite('E:/dataset/net/random_resize/data/' + str(n) + '.png', data)
        cv.imwrite('E:/dataset/net/random_resize/edge/' + str(n) + '.png', edge)
    elif (f == 2):
        row, col, channel = data.shape
        data = cv.resize(data, [col // 2, row // 2])
        data = cv.resize(data, [col, row])
        cv.imwrite('E:/dataset/net/random_resize/data/' + str(n) + '.png', data)
        cv.imwrite('E:/dataset/net/random_resize/edge/' + str(n) + '.png', edge)
    elif (f == 3):
        row, col, channel = data.shape
        data = cv.resize(data, [col // 3, row // 3])
        data = cv.resize(data, [col, row])
        cv.imwrite('E:/dataset/net/random_resize/data/' + str(n) + '.png', data)
        cv.imwrite('E:/dataset/net/random_resize/edge/' + str(n) + '.png', edge)
    else:
        row, col, channel = data.shape
        data = cv.resize(data, [col // 4, row // 4])
        data = cv.resize(data, [col, row])
        cv.imwrite('E:/dataset/net/random_resize/data/' + str(n) + '.png', data)
        cv.imwrite('E:/dataset/net/random_resize/edge/' + str(n) + '.png', edge)
