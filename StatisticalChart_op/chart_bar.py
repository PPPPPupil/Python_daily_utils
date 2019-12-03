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
    # 折线图，x：自定义的名称（数字或其它），y：该x变量的数值
    plt.figure(figsize=(15, 10)) # 画布大小
    plt.plot(x_data, y_data)
    plt.xlabel('this is x')
    plt.ylabel('this is y')
    plt.title(title)
    plt.show()

def draw_Bar(x_data, y_data, title):

    plt.bar(x_data, y_data, width=8, color="red")
    plt.xlabel("x")  # 设置X轴Y轴名称
    plt.ylabel("y")
    plt.xticks(x_data)  # 加此命令可使x坐标位x_data,否则位range(len(x_data))
    plt.title(title)
    # plt.show()
