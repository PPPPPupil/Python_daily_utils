import cv2
import numpy as np
import os


def video2array(path, filename):
    """
    读入path下的filename 视频文件，将所有帧储存为numpy数组（帧数，高，宽，通道=3）
    :param path:
    :param filename:
    :return:
    """
    video_array = []
    cap = cv2.VideoCapture(os.path.join(path, filename))  # 获取视频文件
    while (cap.isOpened()):
        ret, frame = cap.read()
        if frame is not None:
            # 添加该帧
            video_array.append(frame)
        elif frame is None:
            # 视频的最后一帧返回None（若视频帧数cap.get(7)==16帧，则从16帧开始包括16帧，其frame都将返回None）
            break
    video_array = np.array(video_array)
    return video_array
