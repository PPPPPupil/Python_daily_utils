import dicom
import numpy as np
import SimpleITK as sitk


def pixel2hu(filename, path):
    """
    将像素值转换为Hu（CT）值   常用于CT图像
    :param filename: CT图像文件名称
    :param path: CT图像文件所在路径
    :return: Hu值CT
    """
    dcm_path = '图片路径'
    img = dicom.read_file(dcm_path)
    img_array = sitk.GetArrayFromImage(sitk.ReadImage(dcm_path))
    HU = np.dot(img_array, img.RescaleSlope) + img.RescaleIntercept
    return HU
