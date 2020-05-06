"""
读取文件夹下所有文件，并针对文件名称排序
"""
import os


def sort_by_alphabet(path):
    """
    按照首字母顺序排列path下的文件列表
    :param path: 文件所在目录
    :return: 排序后的列表
    """
    file_list = os.listdir(path)
    return file_list


def sort_by_ASCII(path):
    """
    从首字母开始，按照ASCII码对列表进行排序。首字母相同则比较下一位
    :param path: 文件所在目录
    :return: 排序后的列表
    """
    file_list = sorted(os.listdir(path))
    return file_list


def sort_by_figure(path, head=1, tail=-1):
    """
    按照文件名中的数字对文件列表进行排序（要求被排序文件符合相同规则的命名）
    :param path: 文件所在目录
    :param head: （正）文件名中，数字之前的无用字符个数（1代表去掉文件名中前一个字符）
    :param tail: （负）文件名中，数字之后的无用字符个数(包括“.后缀”)（-1代表去掉文件名中最后一个字符，若末尾不去掉字符，则[head：]）
    :return: 排序后的列表

    *注意  list.sort就好，若list = list.sort,会返回None
    """
    file_list = os.listdir(path)
    file_list.sort(key=lambda x: int(x[head:tail]))
    return file_list

# 若文件名中除数字部分，其它部分命名规则一致，则数字部分使用相同位数的命名原则，会使得排列更方便（eg. sample00013.dcm）
