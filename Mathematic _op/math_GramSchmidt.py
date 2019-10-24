"""
对一组一维向量进行施密特正交化处理
"""
from sympy.matrices import Matrix, GramSchmidt
import numpy as np


# =================================数学方法（被实际操作调用）====================================

# 【施密特1】 sympy.matrices包中的施密特正交与自己写的逆正交，采用矩阵形式，没有精度损失
# 使用详解 https://www.cnblogs.com/fengyubo/p/10516798.html 或本文件的GramSchmidt_withArray、inverseGramSchmidt_withArray方法
def GramSchmidt(vlist, orthonormal=False):
    """
    copy from sympy.matrices.GramSchmidt
    :param vlist: 向量组为list，向量组的每一个向量为Matrix
    :param orthonormal:是否正则化
    :return:list[Matrix]


    Example:
    vec_list1 = [Matrix([1, 2, -1]), Matrix([-1, 3, 1]), Matrix([4, 1, 0])]
    gs_list1 = GramSchmidt(vec_list1)
    """
    out = []
    m = len(vlist)
    for i in range(m):
        tmp = vlist[i]
        for j in range(i):
            tmp -= vlist[i].project(out[j])
        if not tmp.values():
            raise ValueError(
                "GramSchmidt: vector set not linearly independent")
        out.append(tmp)
    if orthonormal:
        for i in range(len(out)):
            out[i] = out[i].normalized()
    return out


def inverse_GramSchmidt(gs_list, vlist, orthonormal=False):
    """
    自己写的关于【from sympy.matrices import GramSchmidt】的逆变换
    :param gs_list: 施密特正交后的正交向量组
    :param vlist: 原始未正交的向量组
    :param orthonormal: 是否正则化
    :return:list[Matrix]

    Example:
    ori_list1 = inverse_GramSchmidt(gs_list1,vec_list1)
    """
    out = []
    m = len(gs_list)
    for i in range(m):
        tmp = gs_list[i]
        for j in range(i):
            tmp += vlist[i].project(gs_list[j])
        if not tmp.values():
            raise ValueError(
                "GramSchmidt: vector set not linearly independent")
        out.append(tmp)
    if orthonormal:
        for i in range(len(out)):
            out[i] = out[i].normalized()
    return out


# 【施密特2】 某篇论文的施密特正交与逆施密特正交，由于采用浮点数形式，会损失精度
# 直接传入numpy数组即可
def my_GramSchmidt(vlist, orthonormal=False):
    """

    :param vlist: 原始向量组（array）
    :param orthonormal:是否正则化
    :return:（array）


    Example：
    vec_list = np.array([[1, 2, -1], [-1, 3, 1], [4, 1, 0]])
    gs_list = my_GramSchmidt(vec_list)
    """
    gs_out = []
    v_num = len(vlist)
    # 逐向量正交化
    for i in range(v_num):
        gs_i = vlist[i] - np.mean(vlist[i])
        for j in range(i):
            gs_i -= phy(vlist[i], gs_out[j]) * gs_out[j]
        gs_out.append(gs_i)
    if orthonormal:
        for i in range(len(gs_out)):
            gs_out[i] = gs_out[i].normalized()
    return gs_out


def my_inverseGramSchmidt(gs_list, vlist, orthonormal=False):
    """

    :param gs_list:正则化后向量组（array）
    :param vlist:原始向量组（array）
    :param orthonormal:是否正则化
    :return:（array）


    Example:
    ori_list = my_inverseGramSchmidt(gs_list,vec_list)
    """
    z_out = []
    v_num = len(gs_list)
    # 逐向量正交化
    for i in range(v_num):
        z_i = gs_list[i] + np.mean(vlist[i])
        for j in range(i):
            z_i += phy(vlist[i], gs_list[j]) * gs_list[j]
        z_out.append(z_i)
    if orthonormal:
        for i in range(len(z_out)):
            z_out[i] = z_out[i].normalized()
    return z_out


def phy(vector, gs_vector):
    covariance = np.cov(vector, gs_vector)[0, 1]  # 取两个向量的协方差
    variance = np.var(gs_vector)
    phy_ = covariance / variance
    return phy_


# ==================================【施密特1】的实际操作（传入数组，传出数组）======================
def GramSchmidt_withArray(vector_set, norm=False):
    """
    传入一组一维向量，返回正交化后的向量组
    :param vector_set: 原始向量组，行数代表有多少个一维向量(即每一行是一个一维向量)
    :param norm: 是否将正交化后的向量组正则化
    :return: 正交化后的向量组（每一行是一个一维向量）
    """
    vector_num = vector_set.shape[0]  # 向量个数
    vector_matrix_set = []  # 用于正交计算的向量组矩阵形式

    for i in range(vector_num):
        vector_matrix_set.append(Matrix(vector_set[i, :]))

    gs_matrix_set = GramSchmidt(vector_matrix_set, norm)  # 正交化
    gs_array_set = np.array(gs_matrix_set)  # 转array
    return gs_array_set


def inverseGramSchmidt_withArray(gs_array_set, vector_set, norm=False):
    """
    传入施密特正交后的向量组gs_array_set、未正交之前的原始向量组vector_set，返回未正交之前的原始向量组vector_set
    （没有看错，很鸡肋，必须已知原向量组才能返回原向量组，但是适用于替换gs_array_set某些向量之后的逆变换情况）
    :param gs_array_set:施密特正交后的向量组gs_array_set（每一行是一个一维向量）
    :param vector_set:未正交之前的原始向量组vector_set（每一行是一个一维向量）
    :param norm:是否正则化
    :return:未正交之前的原始向量组vector_set（每一行是一个一维向量）
    """
    gs_num = gs_array_set.shape[0]  # 向量个数
    gs_matrix_set = []  # 正交后向量组矩阵形式
    vector_matrix_set = []  # 原向量组矩阵形式

    for i in range(gs_num):
        gs_matrix_set.append(Matrix(gs_array_set[i, :]))
        vector_matrix_set.append(Matrix(vector_set[i, :]))

    original_matrix_set = inverse_GramSchmidt(gs_matrix_set, vector_matrix_set,norm)  # 逆正交化
    original_array_set = np.array(original_matrix_set)  # 转array
    return original_array_set
