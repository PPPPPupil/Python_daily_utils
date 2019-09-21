"""绘制直方图 ：直方图用于展示数据的分布，X轴为定量数据（区间），不可移动且区间连续；Y轴表示频次/频数占比"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def draw_hist(data, bins=10, density=0, facecolor="blue", edgecolor="black", alpha=0.7, xstep = 50, normed = None, xlabel='区间', ylabel='频次', title='直方图'):
    """
    绘制data的直方图（横坐标为data所有数据的区间，纵坐标为该区间内data数据的频次）
    :param data: 被统计数据（data数据体现为X轴，Y轴为统计数自动生成）
    :param bins: X轴总区间上竖形条的总数（如共分5个区间，bins=10，则每个区间有2个竖形条）
    :param density:
    :param facecolor: 竖形条颜色
    :param edgecolor: 竖形条边框颜色
    :param alpha: 透明度
    :param xstep: 区间的间隔（每xstep为一个小区间）
    :param normed: 是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
    :param xlabel: X轴标题
    :param ylabel: Y轴标题
    :param title: 直方图title
    :return:
    """
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    plt.figure(figsize=(32, 16))  # 设置画布大小
    plt.hist(data, bins=bins, density=density, facecolor=facecolor, edgecolor=edgecolor, alpha=alpha, normed=normed)

    # 设置横坐标间隔
    plt.xticks(np.arange(min(data), max(data), step=xstep))
    # 显示横轴标签
    plt.xlabel(xlabel)
    # 显示纵轴标签
    plt.ylabel(ylabel)
    # 横坐标字号
    plt.tick_params(labelsize=30)
    # 显示图标题
    plt.title(title)
    plt.show()