import os


def get_file_suffix(filenmae):
    """
    返回目标文件后缀名
    :param filenmae: 目标文件名
    :return: 后缀
    """
    name, suffix = os.path.splitext(filenmae)
    return suffix


def get_files_with_suffix(path, suffix='.jpg'):
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


def get_files_with_suffix_from_grandfatherPath(grandfather_path, suffix='.jpg'):
    """
    遍历祖父级目录下，各个父级目录内指定后缀名的文件，返回文件名列表（D://grandfather/father1/target.jpg）
    :param grandfather_path: 祖父级目录
    :param suffix: 指定后缀
    :return:
    """
    father_list = os.listdir(grandfather_path)
    target_list_all = []
    for father_dir in father_list:
        if os.path.isdir(os.path.join(grandfather_path,father_dir)):  # 判断是否为目录
            target_list_tempt = get_files_with_suffix(os.path.join(grandfather_path,father_dir),suffix=suffix)
            target_list_all.extend(target_list_tempt)
        else:
            print("The file named:[" +father_dir+ "] in the grandfather path ["+ grandfather_path+"]is not a dir")
    return target_list_all

