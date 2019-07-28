"""统计图像最小值、最大值、均值、像素值分布"""
import numpy as np
from StatisticalChart_op.chart_histogram import draw_hist


def draw_distrubution(arr):
    """
    绘制像数值直方图分布
    :param arr: 图像数组
    :return:
    """
    arr_flatten = arr.flatten()
    draw_hist(arr_flatten, bins=30, density=0, facecolor="blue", edgecolor="black", alpha=0.7, xstep=2, xlabel='区间',
              ylabel='占比', title='像素值统计直方图')


def get_minmax(arr):
    """
    最小最大值
    :param arr: 图像数组
    :return: 最值
    """
    arr_flaten = arr.flatten()
    min = arr_flaten.min()
    max = arr_flaten.max()
    return min, max


def get_average(arr):
    """
    均值
    :param arr: 图像数组
    :return: 均值
    """
    arr_flatten = arr.flatten()
    average = np.mean(arr_flatten)
    return average
