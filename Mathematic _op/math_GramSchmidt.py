"""
对一组一维向量进行施密特正交化处理
"""
from sympy.matrices import Matrix, GramSchmidt
import numpy as np


def GramSchmidt_withArray(vector_set, norm=False):
    """
    传入一组一维向量，返回正交化后的向量组
    :param vector_set: 原始向量组，行数代表有多少个一维向量
    :param norm: 是否将正交化后的向量组正则化
    :return: 正交化后的向量组
    """
    vector_num = vector_set.shape[0]  # 向量个数
    vector_matrix_set = []  # 用于正交计算的向量组矩阵形式

    for i in range(vector_num):
        vector_matrix_set.append(Matrix(vector_set[i, :]))

    gs_matrix_set = GramSchmidt(vector_matrix_set, norm)  # 正交化
    gs_array_set = np.array(gs_matrix_set)  # 转array
    return gs_array_set
