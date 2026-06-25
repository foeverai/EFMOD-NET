import os
import cv2
from tqdm import tqdm

def split_train_val(image_path,labels_path,save_path=None):
    """
    将文件夹下85%的图像作为训练集，15%作为验证集
    Args:
        image_path: 需要分配的图片所在路径
        labels_path: 对应的标签所在路径

    Returns:None

    """
    img_list = os.listdir(image_path)
    # label_list = os.listdir(labels_path)
    img_num = len(img_list)

    # 这里的图像和标签的名字是一样的，所以我们需要获得图像的文件名即可
    for i,img in enumerate(tqdm(img_list)):
        img_redpath = os.path.join(image_path,img)      # 获取图像文件的完整路径
        label_redpath = os.path.join(labels_path,img)   # 获取对应标签文件的完整路径
        image = cv2.imread(img_redpath,cv2.IMREAD_UNCHANGED)
        label = cv2.imread(label_redpath,cv2.IMREAD_UNCHANGED)

        if save_path:
            train_path = os.path.join(save_path, 'train')
            val_path = os.path.join(save_path, 'val')
        else:
            save_data_path = r'../data/Massachusetts_pad'
            train_path = os.path.join(save_data_path, 'train')
            val_path = os.path.join(save_data_path, 'val')
        # 按照85%训练集，15%验证集进行分割数据集
        if i < int(0.85*img_num):
            image_train = os.path.join(train_path,'img_dir')
            label_train = os.path.join(train_path,'ann_dir')
            if not os.path.exists(image_train):
                os.makedirs(image_train)
            if not os.path.exists(label_train):
                os.makedirs(label_train)
            cv2.imwrite(os.path.join(image_train,img),image)
            cv2.imwrite(os.path.join(label_train,img),label)
        else:
            image_val = os.path.join(val_path, 'img_dir')
            label_val = os.path.join(val_path, 'ann_dir')
            if not os.path.exists(image_val):
                os.makedirs(image_val)
            if not os.path.exists(label_val):
                os.makedirs(label_val)
            cv2.imwrite(os.path.join(image_val, img), image)
            cv2.imwrite(os.path.join(label_val, img), label)

if __name__ == '__main__':
    image_path = r'H:/BaiduNetdiskDownload/Massachusetts/filter_pad_image'
    labels_path = r'H:/BaiduNetdiskDownload/Massachusetts/filter_pad_labels'
    save_path = r'H:/BaiduNetdiskDownload/Massachusetts/Massachusetts_data'
    split_train_val(image_path,labels_path,save_path)


