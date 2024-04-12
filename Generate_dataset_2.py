import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import interpolate
from scipy.signal import argrelextrema
import pandas as pd

random.seed(1143)

x_list = []
y_list = []
x_extreme_point = []
y_extreme_point = []
x_pix_list = []
y_pix_list = []
data = []


def plt_init(grid, color, axes_background_color, grid_color_random, grid_linewidth_random):
    plt.clf()
    plt.axes(facecolor=color[axes_background_color], alpha=0)
    if (grid >= 1):
        plt.grid(b=1, color=color[grid_color_random], linewidth=grid_linewidth_random)
    else:
        plt.grid(b=0)
    plt.xlim([0, 100])
    plt.ylim([0, 100])


def plt_init2():
    plt.clf()
    plt.axis('off')
    plt.grid(b=0)
    plt.xlim([0, 100])
    plt.ylim([0, 100])

def plot_data(m):
    print(m)
    plt.clf()
    plt.figure(figsize=(6.4, 4.8))  # box left=80 right=575 up=58 down=427

    n = 50  # 生成n个点
    # x轴参数
    x = np.linspace(0, 100, n)
    x_pix = np.linspace(0, 100, 496)

    # y轴参数
    y = np.random.randint(10, 90, n)
    y_interpolate = interpolate.interp1d(x, y, kind='quadratic')
    # y_interpolate = interpolate.interp1d(x, y, kind='cubic')
    y_pix = y_interpolate(x_pix)

    # 生成的点和像素点
    x_list.append(x)
    y_list.append(y)
    x_pix_list.append(x_pix)
    y_pix_list.append(y_pix)

    # 极值点
    x_extreme_point_temp = []
    y_extreme_point_temp = []
    x_extreme_point_temp.append(x_pix[0])
    y_extreme_point_temp.append(y_pix[0])
    if (y_pix[1] > y_pix[0]):
        f = 1
    else:
        f = -1
    for i in range(1, 494):
        if (f == 1):
            if (y_pix[i] > y_pix[i + 1]):
                f = -f
                x_extreme_point_temp.append(x_pix[i])
                y_extreme_point_temp.append(y_pix[i])
        if (f == -1):
            if (y_pix[i] < y_pix[i + 1]):
                f = -f
                x_extreme_point_temp.append(x_pix[i])
                y_extreme_point_temp.append(y_pix[i])
    x_extreme_point_temp.append(x_pix[495])
    y_extreme_point_temp.append(y_pix[495])

    x_extreme_point.append(x_extreme_point_temp)
    y_extreme_point.append(y_extreme_point_temp)

    # color参数
    color = ['r', 'g', 'b', 'azure', 'dimgray', 'lavenderblush', 'lightyellow',
             'mediumpurple', 'moccasin', 'olive', 'darkorange', 'brown', 'darkviolet',
             'lime', 'coral', 'sandybrown', 'silver', 'plum', 'black',
             'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
    n_color = len(color)
    line_color_random = np.random.randint(0, n_color - 12)
    grid_color_random = np.random.randint(0, n_color)
    while (color[line_color_random] == color[grid_color_random]):
        line_color_random = np.random.randint(0, n_color - 12)
        grid_color_random = np.random.randint(0, n_color)

    # 线宽参数
    linewidth_random = np.random.random(1) * 5 + 1

    # 网格线
    grid = np.random.randint(0, 3)
    grid_linewidth_random = np.random.random(1) * 2 + 1
    while (linewidth_random < grid_linewidth_random + 1):
        linewidth_random = np.random.random(1) * 5 + 1
        grid_linewidth_random = np.random.random(1) * 2 + 1

    # 背景色
    axes_background_color = np.random.randint(0, n_color)
    while (axes_background_color == line_color_random or axes_background_color == grid_color_random):
        axes_background_color = np.random.randint(0, n_color)
    # plt.axes(facecolor=color[axes_background_color], alpha=0)


    # 画图
    plt_init(grid, color, axes_background_color, grid_color_random, grid_linewidth_random)
    plt.plot(x_pix, y_interpolate(x_pix), color=color[line_color_random], linewidth=1)
    plt.savefig("dataset/net/1/data/" + str(m) + ".png")

    plt_init(grid, color, axes_background_color, grid_color_random, grid_linewidth_random)
    plt.plot(x_pix, y_interpolate(x_pix), color=color[line_color_random], linewidth=3)
    plt.savefig("dataset/net/3/data/" + str(m) + ".png")

    plt_init(grid, color, axes_background_color, grid_color_random, grid_linewidth_random)
    plt.plot(x_pix, y_interpolate(x_pix), color=color[line_color_random], linewidth=5)
    plt.savefig("dataset/net/5/data/" + str(m) + ".png")

    plt_init(grid, color, axes_background_color, grid_color_random, grid_linewidth_random)
    plt.plot(x_pix, y_interpolate(x_pix), color=color[line_color_random], linewidth=linewidth_random)
    plt.savefig("dataset/net/random/data/" + str(m) + ".png")

    # mask
    plt_init2()
    plt.plot(x_pix, y_interpolate(x_pix), color='black', linewidth=1)
    plt.savefig("dataset/net/1/mask/" + str(m) + ".png")

    plt_init2()
    plt.plot(x_pix, y_interpolate(x_pix), color='black', linewidth=3)
    plt.savefig("dataset/net/3/mask/" + str(m) + ".png")

    plt_init2()
    plt.plot(x_pix, y_interpolate(x_pix), color='black', linewidth=5)
    plt.savefig("dataset/net/5/mask/" + str(m) + ".png")

    plt_init2()
    plt.plot(x_pix, y_interpolate(x_pix), color='black', linewidth=1)
    plt.savefig("dataset/net/random/mask_1/" + str(m) + ".png")

    plt_init2()
    plt.plot(x_pix, y_interpolate(x_pix), color='black', linewidth=linewidth_random)
    plt.savefig("dataset/net/random/mask_random/" + str(m) + ".png")


if __name__ == "__main__":
    n = 1000
    for i in range(0, n):
        plot_data(i)

    for i in range(0, n):
        data.append(x_list[i])
        data.append(y_list[i])
        data.append(x_extreme_point[i])
        data.append(y_extreme_point[i])
        data.append(x_pix_list[i])
        data.append(y_pix_list[i])

    df = pd.DataFrame(data, dtype=float)
    df.to_csv('dataset/net/result.csv', index=False, header=False)
