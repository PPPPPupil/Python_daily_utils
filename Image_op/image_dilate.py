"""
将二值形态图像进行膨胀（单张或对多通道逐层单张）
"""
from skimage import morphology


def dilate_single(binary_image_array, radius=4):
    """
    将二值化图像以radius个像素进行膨胀(morphology.disk(radius):默认以圆形进行膨胀)
    :param binary_image_array: 二值二维数组
    :param radius: 膨胀系数
    :return: 膨胀后图像
    """
    image_dilated = morphology.dilation(binary_image_array, morphology.disk(radius))
    return image_dilated


def dilateBySlice(binary_image_array, radius):
    """
    逐层膨胀，使用cv2.dilate(img,kernel,iterations = 1)也是逐层，但找不到合适的形状
    而morphology.dilation只能处理单通道图像
    传入arr多通道数组，逐通道膨胀
    :param binary_image_array: 二值三维数组
    :param radius: 膨胀系数
    :return: 膨胀后图像
    """
    arrd = binary_image_array.copy()
    total_channels = binary_image_array.shape[2]
    for i in range(total_channels):
        arrd[:, :, i] = morphology.dilation(binary_image_array[:, :, i], morphology.disk(radius))

    # return arrd.astype(np.uint8)  # TODO: 保存多通道图象时，只接受uint8格式，而不能float
    return arrd
