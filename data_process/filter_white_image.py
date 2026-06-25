##筛选图像中白色区域较多的影像并删除

import os
import cv2
import numpy as np
import shutil
from tqdm import tqdm

#影像路径
img_path = r'H:/BaiduNetdiskDownload/Massachusetts/image'
#标签路径
label_path = r'H:/BaiduNetdiskDownload/Massachusetts/labels'
#筛选影像保存路径
imsa_path = r'H:/BaiduNetdiskDownload/Massachusetts/filter_image'
#对应标签保存路径
lasa_path = r'H:/BaiduNetdiskDownload/Massachusetts/filter_labels'
#空白阈值，这里我设置为0.1,可根据数据集调整
rat = 0.1

name = os.listdir(img_path)
fuhe = []
for i in tqdm(name):
    img = cv2.imread(img_path+'/'+ i,-1)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype(np.uint32)
    # img = np.float32(img)
    cd = np.unique(img)
    # xx 为统计各个像素值的数量列表
    xx = np.bincount(img.flatten(),minlength=256)
    cout = xx[255]
    zong = img.shape[0]*img.shape[1]
    if cout/zong < rat:
        fuhe.append(i)
#创建保存文件夹路径
if not os.path.exists(imsa_path):
    os.makedirs(imsa_path)
if not os.path.exists(lasa_path):
    os.makedirs(lasa_path)
for i in fuhe:
    #移动
    # shutil.move(img_path,imsa_path)
    # shutil.move(label_path,lasa_path)
    #复制完移动
    shutil.copyfile(img_path+'/'+i,imsa_path+'/'+i)
    shutil.copyfile(label_path+'/'+i.replace('.tiff','.tif'),lasa_path+'/'+i)
