import os
import sys
from PIL import Image, ImageSequence


# path = sys.path[0]                          # 设置路径 -- 系统当前路径
def gif_reverse(filename, source_path, save_path):
    """
    读入gif，并倒序保存
    :param filename: gif文件全名
    :param source_path: gif所在路径
    :param save_path: 倒序gif保存路径
    :return:
    """
    with Image.open(os.path.join(source_path,filename)) as im:
        if im.is_animated:
            frames = [f.copy() for f in ImageSequence.Iterator(im)]
            frames.reverse()  # 内置列表倒序
            frames[0].save(os.path.join(save_path,  filename + '_reversed.gif'), save_all=True,
                           append_images=frames[1:])  # 保存
