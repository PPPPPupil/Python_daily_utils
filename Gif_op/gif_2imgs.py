"""逐张保存gif图像"""
from PIL import Image
import os

def gif2images(filename, source_path, save_path):
    """
    读取一个gif文件，并将其拆分为序列图像储存
    :param filename:  gif文件全名
    :param source_path:  gif文件所在目录
    :param save_path:  序列图像保存目录
    :return:
    """
    im = Image.open(os.path.join(source_path,filename))
    try:
        im.save(os.path.join(save_path, filename+'_{:02d}.png'.format(im.tell())))
        while True:
            im.seek(im.tell() + 1)
            im.save(os.path.join(save_path, filename+'_{:02d}.png'.format(im.tell())))
    except:
        print("处理结束")

