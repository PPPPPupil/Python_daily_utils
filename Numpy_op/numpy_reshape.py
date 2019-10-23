import numpy as np

# reshape ！= resize，reshape不改变数组元素的个数，仅改变数组的维度

# 多维转1维
arr_duowei = np.random.random((3, 3))
arr_1wei1 = arr_duowei.flatten()
arr_1wei2 = arr_duowei.reshape(arr_duowei.shape[0] * arr_duowei.shape[1])

# 1维转多维(9=3*3)
arr_1wei = np.random.random(9)
arr_duowei1 = arr_1wei.reshape(3, 3)

# 多维转多维(a1*a2*a3 = b1*b2)
arr_duowei_1 = np.random.random((a1,a2,a3))
arr_duowei_2 = arr_duowei_1.reshape(b1,b2)