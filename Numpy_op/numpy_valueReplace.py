import numpy as np


def setMin(arr, Tmin):
    """
    使传入的arr数组最小值为0Tmin 方法13不改变原始arr，方法2改变原始数组，所以要基于copy执行
    arr:目标数组
    Tmin:目标数组的目标最小值（小于Tmin一律替换为Tmin）
    """

    # 方式1:逐元素对比arr的元素与Tmin，取其中较大值
    arr_new = np.maximum(arr, Tmin)

    # 方式2:找出小于Tmin的点置换为Tmin
    arr_new = arr.copy()
    arr_new[arr_new < Tmin] = Tmin

    # 方式3:当满足condition，返回arr，否则返回Tmin
    arr_new = np.where(arr > Tmin, arr, Tmin)

    return arr_new


def setMax(arr, Tmax):
    """
    使传入的arr数组最大值为Tmax  方法13不改变原始arr，方法2改变原始数组，所以要基于copy执行
    arr:目标数组
    Tmax:目标数组的目标最大值（小于Tmax一律替换为Tmax）
    """

    # 方式1:逐元素对比arr的元素与Tmax，取其中较小值
    arr_new = np.minimum(arr, Tmax)

    # 方式2:找出大于Tmax的点置换为Tmax
    arr_new = arr.copy()
    arr_new[arr_new > Tmax] = Tmax

    # 方式3:当满足condition，返回arr，否则返回Tmax
    arr_new = np.where(arr < Tmax, arr, Tmax)

    return arr_new
