# Python_daily_utils
此文件夹应有两个.h5格式的权重文件，名称分别为 "inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5 "和 "full_version_weigths.h5" 。

其中，"inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5"为使用ImageNet预训练的Inception_ResNet网络的预加载权重，需要从【https://github.com/fchollet/deep-learning-models/releases/download/v0.7/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5】下载。（Inception_ResNet在代码中用于提取1000维度图像特征（embed_input））; 
"full_version_weigths.h5"为本网络的权重，每次训练都可以选择生成。

