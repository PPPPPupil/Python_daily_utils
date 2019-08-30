import os

def get_file_suffix(filenmae):
    """
    返回目标文件后缀名
    :param filenmae: 目标文件名
    :return: 后缀
    """
    name, suffix = os.path.splitext(filenmae)
    return suffix

def get_files_with_suffix(path, suffix = '.jpg'):
    """
    返回目标路径下，包含指定后缀名的文件列表
    :param path: 目标路径
    :param suffix: 指定后缀名
    :return: 指定文件列表
    """
    file_list = os.listdir(path)
    target_list = []
    for filename in file_list:
        if os.path.splitext(filename)[1] == suffix:
            target_list.append(filename)
    return target_list
