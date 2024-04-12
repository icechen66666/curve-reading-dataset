import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

for n in range(1000):
    print(n)
    img = cv.imread('dataset/net/random/data/' + str(n) + '.png')
    col = img.shape[1]  # 640
    row = img.shape[0]  # 480

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    r_random = np.random.randint(-10, 10)
    g_random = np.random.randint(-10, 10)
    b_random = np.random.randint(-10, 10)

    img[:, :, 0] = img[:, :, 0] + r_random
    img[:, :, 1] = img[:, :, 1] + g_random
    img[:, :, 2] = img[:, :, 2] + b_random

    img = np.clip(img, 0, 255)

    # plt.imshow(img)
    # plt.show()

    cv.imwrite('dataset/net/random/augmented/' + str(n) + '.png', img)
