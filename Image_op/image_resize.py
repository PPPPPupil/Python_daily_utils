"""resize 图像大小"""

from skimage.transform import resize


def resize_image(image_arr, targetSize=(256,256), preserve_range=True, mode='constant'):
    """
    将图像裁剪/扩展到制定大小
    :param image_arr:  被裁减图像数组
    :param targetSize:  目标大小（r,c,...）
    :param preserve_range: 是否使结果保持与原始图像同样的像素值范围（True不变，False归一化到0-1）
    :param mode: 边界区域的填充方式
    :return: 裁剪/扩展后的图像
    """
    image_resized = resize(image_arr, targetSize, preserve_range=preserve_range, mode=mode)

    # return image_resized.astype(np.uint8)  # TODO: uint8 损失精度,但方便储存图像
    return image_resized


