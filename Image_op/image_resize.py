"""resize 图像大小"""

from skimage.transform import resize
import cv2


def cv2Resize(arr, dsize, dst=None, fx=None, fy=None, interpolation=None):
    """
    :param arr: 输入，原图像，即待改变大小的图像；
    :param dsize: 输出，改变大小之后的图像，这个图像和原图像具有相同的内容，只是大小和原图像不一样而已；
    :param dst: 输出图像的大小。如果这个参数不为0，那么就代表将原图像缩放到这个Size(width，height)指定的大小；如果这个参数为0，那么原图像缩放之后的大小就要通过下面的公式来计算：
       dsize = Size(round(fx*src.cols), round(fy*src.rows)),其中，fx和fy就是下面要说的两个参数，是图像width方向和height方向的缩放比例。
    :param fx: width方向的缩放比例，如果它是0，那么它就会按照(double)dsize.width/src.cols来计算；
    :param fy: height方向的缩放比例，如果它是0，那么它就会按照(double)dsize.height/src.rows来计算；
    :param interpolation: 这个是指定插值的方式，图像缩放之后，肯定像素要进行重新计算的，就靠这个参数来指定重新计算像素的方式，有以下几种：
      INTER_NEAREST - 最邻近插值
      INTER_LINEAR - 双线性插值，如果最后一个参数你不指定，默认使用这种方法
      INTER_AREA -区域插值 resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
      INTER_CUBIC - 4x4像素邻域内的双立方插值
      INTER_LANCZOS4 - 8x8像素邻域内的Lanczos插值
    :return:
    """
    arr_res = cv2.resize(src=arr, dsize=dsize, dst=dst, fx=fx, fy=fy, interpolation=interpolation)
    # return arr_res.astype(np.uint8)  # TODO: uint8 损失精度,但某些情况下方便查看图像
    return arr_res


# def resize_image(image_arr, targetSize=(256, 256), preserve_range=True, mode='constant'):
#     """
#     将图像裁剪/扩展到制定大小
#     :param image_arr:  被裁减图像数组
#     :param targetSize:  目标大小（r,c,...）
#     :param preserve_range: 是否使结果保持与原始图像同样的像素值范围（True不变，False归一化到0-1）
#     :param mode: 边界区域的填充方式
#     :return: 裁剪/扩展后的图像
#     """
#     image_resized = resize(image_arr, targetSize, preserve_range=preserve_range, mode=mode)
#
#     # return image_resized.astype(np.uint8)  # TODO: uint8 损失精度,但方便储存图像
#     return image_resized
