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
