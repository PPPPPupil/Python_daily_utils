import numpy as np


def hu_clipWL(arr, min=-200, max=200):
    """
    调整窗宽窗位（注意，此处调整的是Hu值-即CT值，而非像素值）
    :param arr: CT图像
    :return: 截断Hu值后的CT图像
    """
    arr = np.clip(arr, min, max, out=arr)
    return arr
