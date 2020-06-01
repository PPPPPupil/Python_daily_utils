import numpy as np
import imageio
from PIL import Image
import os

"""
以不同的颜色，在原始图像中表示label和result
"""
def colorfulLabel(original, label, result, clip=True, Hu=[-1024, 1023]):
    """
     分别以不同颜色在原图中表示金标准和分割结果（区分真假阳性-绿红，真假阴性）
    :param original: 原始图像
    :param label: 金标准
    :param result: 分割结果
    :param clip: 是否对Hu值进行截断
    :param Hu: Hu值范围
    :return: 色彩斑斓的结果示意图
    """


    if clip is True:
        original = np.clip(original, Hu[0], Hu[1])

    coloredResult = np.stack([original,original,original],axis=2)

    # 绿 = label
    coloredResult[:,:,0][label == 255] = 0
    coloredResult[:, :, 1][label == 255] = 255
    coloredResult[:, :, 2][label == 255] = 0
    # 红+绿=黄 = 真阳性
    # 红 = 假阳性， 绿 = 假阴性
    coloredResult[:, :, 0][result == 255] = 255

    return coloredResult

if __name__ == '__main__':
    originalP = r"D:\MyProjects\PycharmProjects\SurgeryNavigation\Data\3Dircadb1\3Dircadb1.6\PATIENT_DICOM\image_58.tif"
    labelP =  r"D:\MyProjects\PycharmProjects\SurgeryNavigation\Data\3Dircadb1\3Dircadb1.6\liverTumorMask\58.tif"
    resultP = r"D:\MyProjects\PycharmProjects\论文\LiverAndLeisionResult_Visualize\leision_6\58.tif"
    original = imageio.imread(originalP).astype(np.uint8)
    label = imageio.imread(labelP).astype(np.uint8)
    result = imageio.imread(resultP).astype(np.uint8)
    coloredResult = colorfulLabel(original, label, result, clip=True, Hu=[60, 400])
    saveP = r'D:\MyFiles\laboratory\汇报\配准肝癌手术规划课题骨干\第一次报告\当前成果reslut部分示例'
    Image.fromarray(coloredResult.astype(np.uint8)).save(os.path.join(saveP,str(6)+'_'+str(58)+'tumor.tif'))


