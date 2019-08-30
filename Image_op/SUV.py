import numpy as np

#编写dicom类
class dicom_PT():
    """
    PET dicom原始文件 转 SUV值
    example：
    PET = dicom_PT(casepath)
    voxel,_ = PET.cal_suv()
    其中：casepath为单个病例pet dicom文件们的上级文件夹
    voxel为返回的SUV数组，以整个病例为单位
    """
    def __init__(self,casepath0,new_spacing=None,lbm=True):
        self.casepath0=casepath0
        # self.new_spacing=new_spacing
        # self.case_path1=casepath0.replace('pet',"ct")
        self.lbm=lbm
        #重采样函数，以便于配准pet和ct     
        #定义一个从pet文件夹计算SUV(bw,lbm)的函数
    def cal_suv(self):
        import pydicom
        import os
        import time
        import datetime
        from matplotlib import pyplot as plt 
        # %matplotlib inline
        # 编码方式,采用utf-8编码
        # import sys
        # # reload(sys)
        # sys.setdefaultencoding('utf8')
        '''arg0为pet图像所在文件夹，arg1为True则进行瘦体重的SUV计算,实验中实际计算的是bw'''
        #读取路径下的pet图像,返回
        PathDicom=self.casepath0
        lstFilesDCM = []  # create an empty list
        for dirName, subdirList, fileList in os.walk(PathDicom):
            for filename in fileList:
        # if ".dcm" in filename.lower():  # check whether the file's DICOM
                lstFilesDCM.append(os.path.join(dirName, filename))
        # 使用pydicom
        # Get ref file
        dic = {}
        #slopes = {} 
        #intercept = {}
        for filepath in lstFilesDCM:
            RefDs = pydicom.read_file(filepath)
            dic[RefDs.InstanceNumber] = filepath
        #slopes[RefDs.InstanceNumber] = RefDs.get('RescaleSlope')
        #intercept[RefDs.InstanceNumber] = RefDs.RescaleIntercept
    #文件数目
        lenf=len(dic)
    #文件维度
        ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))
        ArrayDicom = np.zeros(ConstPixelDims, dtype=np.float32)

        maxv=[]
        for i in range(lenf):
            ds=pydicom.read_file(dic[(i+1)],force=True)

    #if	Corrected	Image	(0x0028,0x0051)	contains	ATTN	and	DECAY	and	Decay	Correction	(0x0054,0x1102)	is	START。

    # if	Units	(0x0054,0x1001)	are	BQML

    #half	life	=	Radionuclide	Half	Life	(0x0018,0x1075)	in	Radiopharmaceutical	Information	Sequence	(0x0054,0x0016) //	seconds

    #核药物信息是一个dataset的列表
            x=ds[0x0054,0x0016].value
    #核素半衰期，单位为秒
            halflife=x[0][0x0018,0x1075].value

    #获取时间和序列时间应该相同也就是，scanDate andTime=SeriesDate and Time

            SeriesDate=ds[0x0008,0x0021]

    #ds[0x0008,0x0031]获取时间和序列时间的具体时间，时分秒

            AcquisitionDate=ds[0x0008,0x0022]



    #start	Time	=	Radiopharmaceutical	Start	Time	(0x0018,0x1072)	in	Radiopharmaceutical	Information	Sequence	(0x0054,0x0016)	
    #start Date	is	not	explicit	…	assume	same	as	Series	Date;	but	consider	spanning	midnight

            startTime = time.strptime(ds[0x0008,0x0021].value+x[0][0x0018,0x1072].value[0:6], '%Y%m%d%H%M%S')

            startTime = datetime.datetime(*startTime[:6])

    #decay	Time	=	scan	Time	– start Time	 //	seconds

            SeriesTime =time.strptime(ds[0x0008,0x0022].value+ds[0x0008,0x0031].value[0:6], '%Y%m%d%H%M%S')

            SeriesTime = datetime.datetime(*SeriesTime[:6])

            decayTime  = SeriesTime-startTime

            decayTime.seconds

    #放射性核素总剂量不针对注射器中的残留剂量进行校正，这里忽略了...

    #injected	Dose	=	Radionuclide	Total	Dose	(0x0018,0x1074)	in	Radiopharmaceutical	Information	Sequence	(0x0054,0x0016) //	Bq

            injectedDose=x[0][0x0018,0x1074].value

    #decayed	Dose	=	injected	Dose	*	pow (2,	-decay	Time	/	half	life)

            decayedDose=injectedDose*pow(2,-decayTime.seconds / halflife)

    #weight	=	Patient's	Weight	(0x0010,0x1030) //	in	kg
        
            weight = ds[0x0010,0x1030].value
    #如果使用瘦体重的话
        
            if self.lbm==True:
                sex = ds[0x0010,0x0040].value
                height=ds[0x0010,0x1020].value
                heightCm=height*100
                if sex == 'F':
                    weight = 1.07 * weight - 148 * (weight / heightCm) ** 2
                else:
                    weight = 1.10 * weight - 120 * (weight / heightCm) ** 2
               #SUVbwScaleFactor	=	(weight	*	1000	/	decayed Dose)

            SUVbwScaleFactor =(float(weight) * 1000.0 / decayedDose)

    #	Rescale	Intercept	is	required	to	be	0	for	PET,	but	use	it	just	in	case

    #	Rescale	slope	may	vary	per	slice	(GE),	and	cannot	be	assumed	to	be	constant	for	the	entire	volume	

    #SUVbw	=	(stored	pixel	value	in	Pixel	Data	(0x7FE0,0x0010)	*	Rescale	Slope	(0x0028,0x1053) +	Rescale	Intercept	(0x0028,0x1052)) *	SUVbwScaleFactor
    #//	g/ml
    #注意此处使用的是suvlbm或者SUVbw，详见前面的weight计算
            SUVbw = (ds.pixel_array*float(ds[0x0028,0x1053].value)+float(ds[0x0028,0x1052].value))*SUVbwScaleFactor                      
            ArrayDicom[:, :, i]=SUVbw
        self.ArrayDicom= ArrayDicom
        self.ds=ds
        return  self.ArrayDicom,self.ds    
    
           
