"""
排序
"""


def sortByKey(num_list, head=1, tail=-1):
    """
    当list中不仅包含数字，还包含无用字符的话，需要使用数字作为关键字对lisy排序
    :param num_list: 被排序list
    :param head: （正）文件名中，数字之前的无用字符个数（1代表去掉元素中前一个字符）
    :param tail: （负）文件名中，数字之后的无用字符个数(包括“.后缀”)（-1代表去掉元素中最后一个字符）
    :return: 排序后的列表
    """
    num_list.sort(key=lambda x: int(x[head:tail]))
    return num_list
