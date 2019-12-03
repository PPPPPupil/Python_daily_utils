"""
逐行读取txt文本到list，两种方法
"""
def load_txt(filepath="example.txt"):
    """
    逐行读取txt文本到list(内存不够用时可以选择逐行读取)
    :param filepath: txt的全路径
    :return:
    """
    list = []
    for line in open(filepath):
        # temp_dice = line.split("str",1)[1]  #对每行内容，按照字符串str将本行分为两部分，取后半部分
        list.append(line)
    return list

def load_txt2(filepath="example.txt"):
    """
    逐行读取txt文本到list（一次性读取内容至内存）
    :param filepath: txt的全路径
    :return:
    """
    with open(filepath) as f:
        lines = f.readlines()
        # temp_dice = line.split("str",1)[1]  #对每行内容，按照字符串str将本行分为两部分，取后半部分

    return lines