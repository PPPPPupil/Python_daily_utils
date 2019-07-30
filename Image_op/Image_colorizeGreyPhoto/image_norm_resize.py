"""可以使用该函数，将图像转为当前网络对应的格式（256，256，channel）、0-255、"""
import numpy
import os
import scipy.misc
from skimage.transform import resize
from PIL import Image
import numpy as np


def load_image(filename, path):
    """
    加载path下filename图像, scipy.misc不会默认将灰度图转换为三通道图像，所以一直在用
    :param filename: 图像文件名称
    :param path: 图像文件所在路径
    :return: 图像数组
    """
    image_array = scipy.misc.imread(os.path.join(path, filename))
    return image_array


def norm_MinMax(arr):
    """
    极值归一化（0-255）
    :param arr:
    :return:
    """
    arr = (arr - arr.min()) / (arr.max() - arr.min()) * 255

    return arr.astype(np.uint8)  # TODO: uint8 损失精度
    # return arr


#  原始图像路径
tempPath = r'D:\Program Files (x86)\JetBrains\PycharmProjects\Coloring-greyscale-images-master\Full-version\tempMedicine'
templist = os.listdir(tempPath)

# 读入图像
imagelist = []
for temp in templist:
    imagelist.append(load_image(temp, tempPath))

# 将图像归一化0-255
image_norm = []
# norm0-255
for image in imagelist:
    image_norm.append(norm_MinMax(image))

#  resize为网络输入大小
image_resize = []
for image in image_norm:
    image_resize.append(resize(image, (256, 256), preserve_range=True, mode='constant'))

# 转换为np数组
image_resize = np.array(image_resize, dtype=np.uint8)
templist = np.array(templist)

# save
for i, image in enumerate(image_resize):
    Image.fromarray(image).save('Test/' + templist[i].split('.')[0] + '.jpg')
