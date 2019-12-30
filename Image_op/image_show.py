"""显示array形式的图像，省去保存步骤直接查看"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def image_show(array, mode='RGB'):
    """
    将array数组作为图像显示，显示效果：显示过程中自动归一化到0-255
    :param array: 数组
    :param mode: 显示形式，RGB：三通道彩色图，gray：灰度图，hot：热图
    （gray、hot仅显示单通道图像时有效,若显示三通道，效果和RGB一致；RGB仅显示三通道为原始图像，若显示单通道图像，很奇怪）
    :return:
    """
    if mode == 'RGB':
        plt.imshow(array)
    elif mode == 'gray':
        plt.imshow(array).set_cmap('gray')
    elif mode == 'hot':
        plt.imshow(array).set_cmap('hot')
    plt.show()
