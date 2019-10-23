import numpy as np


def setMinZero(arr):
    """使传入的arr数组最小值为0  方法13不改变原始arr，方法2改变原始数组，所以要基于copy执行"""

    # 方式1:逐元素对比arr的元素与0，取其中较大值
    arr_new = np.maximum(arr, 0)

    # 方式2:找出小于0的点置换为0
    arr_new = arr.copy()
    arr_new[arr_new < 0] = 0

    # 方式3:当满足condition，返回x，否则返回y
    arr_new = np.where(arr > 0, arr, 0)

    return arr_new
