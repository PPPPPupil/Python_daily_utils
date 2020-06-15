import os
import pydicom
from Dicom_op.SUV import dicom_PT
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

"""以病例为单位，将患者CT、PET、SUV切片储存为体数据"""


def CT_dicom2voxel(case_path, clip=False, minHu=-80, maxHu=300):
    """
    将病例下的CT dicom文件，按照切片序列储存为Hu值体数据
    :param cases_path: 该病例存放CT dicom数据的文件夹
    :param clip: 是否进行Hu值截断
    :param minHu: 最小窗宽
    :param maxHu: 最大窗宽
    :return:
    """
    dicom_list = os.listdir(case_path)
    Hu_voxel = []
    for dicom in dicom_list:
        # 读入dicom文件
        dicom_file = pydicom.read_file(os.path.join(case_path, dicom))
        # 获取图像数组
        pixel_array = dicom_file.pixel_array
        # 根据像素值计算Hu（CT）值
        Hu = np.dot(pixel_array, dicom_file.RescaleSlope) + dicom_file.RescaleIntercept
        # 截断Hu
        if clip == True:
            Hu = np.clip(Hu, minHu, maxHu)

        # 注意这个地方要保证读入的切片和排序切片的顺序一致性（如1之后是10，需要对数字进行排序，1之后成为2）
        Hu_voxel.append(Hu)
    Hu_voxel = np.array(Hu_voxel)
    return Hu_voxel


def PET_dicom2voxel(case_path):
    """
    将病例下的PET dicom文件，按照切片序列储存为PET值体数据
    :param case_path: 该病例存放PET dicom数据的文件夹
    :return:
    """

    dicom_list = os.listdir(case_path)
    PET_voxel = []
    for dicom in dicom_list:
        dicom_file = pydicom.read_file(os.path.join(case_path, dicom))
        pixel_array = (dicom_file.pixel_array).astype(np.float64)
        PET_voxel.append(pixel_array)
    PET_voxel = np.array(PET_voxel)
    return PET_voxel


def SUV_dicom2voxel(case_path):
    """
    将病例下的PET dicom文件，按照切片序列储存为SUV值体数据
    :param case_path: 该病例存放PET dicom数据的文件夹
    :return:
    """
    something = dicom_PT(case_path)
    SUV_voxel, _ = something.cal_suv()
    return SUV_voxel
