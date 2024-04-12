import cv2 as cv
import numpy as np

for n in range(1000):
    img = cv.imread('dataset/net/random/mask_random/' + str(n) + '.png', 0)
    col = img.shape[1]  # 640
    row = img.shape[0]  # 480
    start = 0
    for i in range(col):
        for j in range(row):
            if (img[j][i] < 128):
                start = i
                break
        if (start!=0):
            break
    end = col
    for i in range(col - 1, 0, -1):
        for j in range(row):
            if (img[j][i] < 128):
                end = i
                break
        if (end != col):
            break
    print(str(n) + "  start: " + str(start) + "  end: " + str(end))
    a = []
    b = []
    c = np.ones_like(img) * 255
    for i in range(start, end+1):
        for j in range(row):
            if (img[j][i] < 128):
                a.append(j)
                break
        for j in range(row - 1, 0, -1):
            if (img[j][i] < 128):
                b.append(j)
                break

    for i in range(start, start+len(a)-1):
        if (a[i - 80] < a[i - 79]):
            for j in range(a[i - 80], a[i - 79] + 1):
                c[j][i] = 0
        if (a[i - 80] >= a[i - 79]):
            for j in range(a[i - 80], a[i - 79] - 1, -1):
                c[j][i] = 0
        if (b[i - 80] < b[i - 79]):
            for j in range(b[i - 80], b[i - 79] + 1):
                c[j][i] = 0
        if (b[i - 80] >= b[i - 79]):
            for j in range(b[i - 80], b[i - 79] - 1, -1):
                c[j][i] = 0
    c[a[-1]][end] = 0
    c[b[-1]][end] = 0
    cv.imwrite('dataset/net/random/edge/' + str(n) + '.png', c)
