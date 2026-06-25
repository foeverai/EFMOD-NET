import os
import cv2
from tqdm import tqdm

# 将图片转换成标签二值黑白图
def exchange_black_white(label_path, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print('Created')
    img_list1 = os.listdir(label_path)

    for img_name in tqdm(img_list1):
        image_path = os.path.join(label_path, img_name)
        img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

        if img is not None:
            # 使用NumPy的向量化,将像素变为黑白
            img[img >= 255] = 255
            img[img < 255] = 0

    # 保存修改后的图片
        output_path = os.path.join(save_path, img_name)
        cv2.imwrite(output_path, img)

# 将标签转换成二值图像
def exchange_label(label_path, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print('Created')
    img_list1 = os.listdir(label_path)

    for img_name in tqdm(img_list1):
        image_path = os.path.join(label_path, img_name)
        img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

        if img is not None:
            # 使用NumPy的向量化操作将255替换为1
            img[img == 255] = 1

    # 保存修改后的图片
    #     img_name_new, suiffx = img_name.split('.')
    #     img_name_save = img_name_new+'_mask.'+suiffx

        output_path = os.path.join(save_path, img_name)
        cv2.imwrite(output_path, img)


# 将二值图像转换为gt
def exchange_predic(predict_img_path, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print('Created')
    img_list1 = os.listdir(predict_img_path)

    for img_name in tqdm(img_list1):
        image_path = os.path.join(predict_img_path, img_name)
        img = cv2.imread(image_path)

        if img is not None:
            # 使用NumPy的向量化操作将1替换为255
            img[img == 1] = 255
            # 保存修改后的图片
            output_path = os.path.join(save_path, img_name)
            cv2.imwrite(output_path, img)




if __name__ == '__main__':
    # # 需要转换的标签路径
    image_path = r'G:\mmseg\master_paper_nudt\chapter3_bu\afdanet\afad_deep\vis'
    # # 转换后标签的保存路径
    image_save = r'G:\mmseg\master_paper_nudt\chapter3_bu\afdanet\afad_deep\vis_pre'

    exchange_predic(image_path, image_save)
    # exchange_label(image_path, image_save)
    # exchange_predic(image_path, image_save)


    # exchange_predic(image_path, image_save)

    # pre_img_path = 'H:/mmseg/mmsegmentation-main/data/Deep_Globe_1024x1024/ann_dir/val'
    # save_path = 'H:/mmseg/mmsegmentation-main/data/Deep_Globe_1024x1024/ann_dir/val_gt'
    # exchange_predic(pre_img_path,save_path)

