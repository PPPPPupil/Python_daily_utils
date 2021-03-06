"""
加载外存中图像文件
"""
import os
import scipy
import scipy.misc
import pydicom
import imageio
import cv2
import nibabel as nib
from pydicom import dcmread


def load_image(filename, path):
    """
    加载path下filename图像, scipy.misc不会默认将灰度图转换为三通道图像，所以一直在用。(tif、png、jpg、bmp)
    sicpy1.2.0版本之后，scipy,misc存取图像的方式将被移除，可以使用imageio来替代
    :param filename: 图像文件名称
    :param path: 图像文件所在路径
    :return: 图像数组
    """
    image_array = scipy.misc.imread(os.path.join(path, filename))
    return image_array


def load_hdr_image(filename, path):
    """
    hdr(高动态范围图像)通常以hdr或tif为后缀，需要通过imageio读取保证值不变，否则会压缩到0-255
    :param filename:
    :param path:
    :return:
    """
    image_array = imageio.imread(os.path.join(path, filename))
    return image_array


def load_cv2_image(filename, path):
    """
    cv2中有很多好用的图像处理方法，但cv2默认的读取rgb图像的结果为bgr（不知为何要这么设定），所以使用cv2相关库函数的时候最好还是使用cv2.imread
    :param filename:
    :param path:
    :return:
    """
    image_array = cv2.imread(os.path.join(path, filename))
    return image_array


def load_dicom_image(filename, path):
    """
    加载path下dicom格式文件，并返回其图像的pixel数组（不包含个人信息）
    note:此时读取出来的是像素值，而不是CT（HU）值
    :param filename: dicom图像文件名称
    :param path: dicom图像文件所在路径
    :return: dicom所包含的像素数组
    """
    # dicom_file = dcmread(os.path.join(path,filename))
    dicom_file = pydicom.read_file(os.path.join(path, filename))  # 通过两种方式读入的dicom_file相同
    image_array = dicom_file.pixel_array
    return image_array


def load_nii_image(filename, path):
    """
    读取nii格式的文件，返回其图像像素的array数组
    :param filename: nii图像文件名称
    :param path: nii图像文件所在路径
    :return: nii所包含的像素数组
    """
    nii_file =nib.load(os.path.join(path, filename))
    image_array = img_arr = nii_file.get_fdata()
    return image_array
