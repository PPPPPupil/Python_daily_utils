"""
将图像数组储存为图像文件
"""
import os
from PIL import Image
import numpy as np


def save_image(image_array, save_dir, image_name, regex='.jpg'):
    """
    将单个二维数组或三通道的三维数组储存为图像文件
    :param image_array: 数组
    :param save_dir: 目标路径
    :param image_name: 图像名称
    :param regex: 后缀名
    :return:
    """
    if len(image_array.shape) == 2:
        return Image.fromarray(image_array).save(os.path.join(save_dir, str(image_name) + regex))
    elif len(image_array.shape) == 3:
        """
        在使用时，发现无法利用Image类将float格式数组储存为三通道图像；需将数组转换为uint8格式，此过程可能会损失精度
        """
        image_array = image_array.astype(np.uint8)
        return Image.fromarray(image_array).save(os.path.join(save_dir, str(image_name) + regex))
