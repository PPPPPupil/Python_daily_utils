import os
import shutil

path = r"文件夹路径"
filename = '具体文件.后缀'

#  删除文件
os.remove(os.path.join(path, filename))

#  删除空的文件夹
os.rmdir(path)

#  递归清空含有文件的文件夹（似乎也会删除path文件夹本身）
shutil.rmtree(path)


#  删除文件名中含有某指定元素的文件s
def removeSpecifyFiles(path, picElement='element'):
    """
    删除path路径下，文件名中含有 picElement 的所有文件（文件，而非目录）
    :param path:
    :param picElement:
    :return:
    """
    all_files = os.listdir(path)
    for file in all_files:
        if picElement in file:
            os.remove(os.path.join(path, file))
