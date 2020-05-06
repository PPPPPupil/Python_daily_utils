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
        temp_line = line.split("\n",1)[0]  #每行内容按照字符串\n将本行分为两部分，取q前半部分（去掉结尾回车）
        list.append(temp_line)
    return list

def load_txt2(filepath="example.txt"):
    """
    逐行读取txt文本到list（一次性读取内容至内存）
    :param filepath: txt的全路径
    :return:
    """
    list = []
    with open(filepath) as f:
        lines = f.readlines()
    # 每行内容按照字符串\n将本行分为两部分，取q前半部分（去掉结尾回车）
    for line in lines:
        temp_line = line.split("\n",1)[0]
        list.append(temp_line)
    return list