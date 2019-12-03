"""柱状图： 柱状图用于比较数据的大小，X轴为分类数据，可随意排序；Y轴表示该类数据的数值大小"""

import matplotlib.pyplot as plt


def draw_plot(x_data, y_data, title):
    """
    绘制柱状图（X与Y轴数据一一对应且需手动给出）
    :param x_data: X轴数据
    :param y_data: 与X轴数据一一对应的Y轴数据
    :param title: 柱状图title
    :return:
    """
    # 柱状图，x：自定义的名称（数字或其它），y：该x变量的数值
    fig, axes_lst = plt.subplots()  # 创建窗口以及子图
    axes_lst.plot(x_data, y_data)
    axes_lst.set_title(title)
    plt.show()

def draw_Bar(x_data, y_data, title):
    plt.figure(figsize=(15, 10))
    plt.bar(x_data, y_data, width=8, color="red")
    plt.xlabel("x")  # 设置X轴Y轴名称
    plt.ylabel("y")
    plt.title(title)
    # plt.show()
