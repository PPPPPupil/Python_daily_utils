"""
加载外存中图像文件
"""
import os
import scipy
import scipy.misc
def load_image(filename, path):
    """
    加载path下filename图像, scipy.misc不会默认将灰度图转换为三通道图像，所以一直在用
    :param filename: 图像文件名称
    :param path: 图像文件所在路径
    :return: 图像数组
    """
    image_array = scipy.misc.imread(os.path.join(path, filename))
    return image_array