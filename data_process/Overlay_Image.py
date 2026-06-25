import os
import numpy as np
import cv2
from tqdm import tqdm

def create_data(image_path1:str,image_path2:str):
    # 获取图像和其训练结果数据
    image_list1 = os.listdir(image_path1)
    image_list2 = os.listdir(image_path2)

    img_list1 = sorted(image_list1, key=lambda x: int(os.path.splitext(x.split('.')[0])[0]))
    img_list2 = sorted(image_list2, key=lambda x: int(os.path.splitext(x.split('.')[0])[0]))

    for i in tqdm(range(len(img_list1))):
        img1_file = os.path.join(image_path1,img_list1[i])
        img2_file = os.path.join(image_path2,img_list2[i])
        # 读取数据和预测结果
        img1 = cv2.imread(img1_file)
        pre_img2 = cv2.imread(img2_file,cv2.IMREAD_GRAYSCALE)

        if img1 is not None:
            img1[pre_img2 == 1] = (255,255,255)
        file_name = os.path.join('../data/DP_cat/train',img_list2[i])
        cv2.imwrite(file_name,img1)




if __name__ == '__main__':
    path = 'H:/mmseg/mmsegmentation-main/data/Deep_Globe_1024x1024/img_dir/val'
    path2 = 'H:/mmseg/roadseg/RMFMNet/deepglobe/rmfm_2_dp'
    create_data(path,path2)




