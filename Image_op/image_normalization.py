"""
对图像进行归一化
"""
import numpy as np


def norm_MinMax(arr):
    """
    极值归一化（0-255）
    :param arr:
    :return:
    """
    arr = (arr - arr.min()) / (arr.max() - arr.min()) * 255

    # return arr.astype(np.uint8)  # TODO: uint8 损失精度
    return arr
