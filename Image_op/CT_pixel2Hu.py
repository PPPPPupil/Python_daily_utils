import os
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
    dcm_path = os.path.join(path,filename)
    dicom_file = dicom.read_file(dcm_path)
    pixel_array = dicom_file.pixel_array  # 像素值
    CT_array = np.dot(pixel_array, dicom_file.RescaleSlope) + dicom_file.RescaleIntercept
    # img_array = sitk.GetArrayFromImage(sitk.ReadImage(dcm_path))

    return CT_array
