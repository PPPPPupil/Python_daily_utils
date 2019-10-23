"""
对图像进行归一化
"""
import numpy as np


def norm_MinMax(arr, arrmax=255):
    """
    极值归一化0-arrmax（0-255）
    :param arr:
    :param arrmax:
    :return:
    """
    arr = (arr - arr.min()) / (arr.max() - arr.min()) * arrmax

    # return arr.astype(np.uint8)  # TODO: uint8 损失精度
    return arr
