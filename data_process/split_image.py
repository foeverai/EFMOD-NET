'''Data preprocessing'''
import os
import re
import PIL
import PIL.Image
from tqdm import tqdm
from PIL import Image
import torchvision
import cv2
import numpy as np



'''随机裁剪图片和标签'''
def rand_crop(img, label, height, width):
    """随机裁剪特征和标签图像"""
    rect = torchvision.transforms.RandomCrop.get_params(
        img, (height, width))
    feature = torchvision.transforms.functional.crop(img, *rect)
    label = torchvision.transforms.functional.crop(label, *rect)
    return feature, label




def seg_image(root_path, output_path, spsize_w, spsize_h, img_type):
    """
    将大图像分割成小图像
    Args:
        root_path: 图像的文件位置
        output_path: 输出位置
        spsize_w: 分割的宽
        spsize_h: 分割的高
        img_type: 后缀

    Returns:

    """
    output_path = output_path + '/'
    # img_loacl_num = -1
    img_seg_num = -1
    if os.path.exists(output_path):
        print('save path exist!')
    else:
        os.makedirs(output_path)
        print('save path created!')
    image_list1 = os.listdir(root_path)
    if len(image_list1)<2:
        image_list = image_list1
    else:
        image_list = sorted(image_list1, key=lambda x: int(re.search(r'\d+', x).group()))
    for data in tqdm(image_list):
        suffix = data.split('.')[-1]  # get the suffix
        # img_loacl_num += 1
        image_tiff = PIL.Image.open(root_path + '/' + data)
        # 获得图像的尺寸，宽和高
        weight, higth = image_tiff.size
        # 计算分割的高宽的个数
        weight_num = weight//spsize_w
        higth_num = higth//spsize_h

        if weight/spsize_w-weight_num != 0:
            flag_w = True
        else:
            flag_w = False
        if higth/spsize_h-higth_num != 0:
            flag_h =True
        else:
            flag_h =False

        # 如果大图像长宽正好是小图像的倍数，则正好可以等分：
        if flag_w == False and flag_h == False:
            for i in range(weight_num):
                for j in range(higth_num):
                    # 计算分块图像的像素区域
                    left_star_w = i * spsize_w
                    left_star_h = j * spsize_h
                    right_end_w = left_star_w + spsize_w
                    right_end_h = left_star_h + spsize_h

                    # 获得对应区域的图像
                    image_part = image_tiff.crop((left_star_w, left_star_h, right_end_w, right_end_h))

                    # 保存分割图像到指定的文件夹
                    img_seg_num +=1
                    image_part.save(output_path + '{0}_{1}.{2}'.format(img_type, img_seg_num, suffix))
            # img_seg_num = -1
        # 宽可整除，高不可整除
        elif flag_w ==True and flag_h == False:
            for i in range(weight_num):
                for j in range(higth_num):
                    # 计算分块图像的像素区域
                    left_star_w = i * spsize_w
                    left_star_h = j * spsize_h
                    right_end_w = left_star_w + spsize_w
                    right_end_h = left_star_h + spsize_h

                    # 获得对应区域的图像
                    image_part = image_tiff.crop((left_star_w, left_star_h, right_end_w, right_end_h))

                    # 保存分割图像到指定的文件夹
                    img_seg_num +=1
                    image_part.save(output_path + '{0}_{1}.{2}'.format(img_type, img_seg_num, suffix))
            for k in range(weight_num):
                left_star_h = higth - spsize_h
                left_star_w = k * spsize_w
                right_end_h = higth
                right_end_w = left_star_w + spsize_w

                # 获得对应区域图像
                image_part = image_tiff.crop((left_star_w, left_star_h, right_end_w, right_end_h))

                # 保存分割图像到指定文件夹
                img_seg_num += 1
                image_part.save(output_path + '{0}_{1}.{2}'.format(img_type, img_seg_num, suffix))
            # img_seg_num = -1
        # 当宽和高均不能被整除
        elif flag_w == True and flag_h == True:
            for i in range(weight_num):
                for j in range(higth_num):
                    # 计算分块图像的像素区域
                    left_star_w = i * spsize_w
                    left_star_h = j * spsize_h
                    right_end_w = left_star_w + spsize_w
                    right_end_h = left_star_h + spsize_h

                    # 获得对应区域的图像
                    image_part = image_tiff.crop((left_star_w, left_star_h, right_end_w, right_end_h))

                    # 保存分割图像到指定的文件夹
                    img_seg_num += 1
                    image_part.save(output_path + '{0}_{1}.{2}'.format(img_type, img_seg_num, suffix))
            # 分割底边缘
            for k in range(weight_num):
                left_star_h = higth - spsize_h
                left_star_w = k * spsize_w
                right_end_h = higth
                right_end_w = left_star_w + spsize_w

                # 获得对应区域图像
                image_part = image_tiff.crop((left_star_w, left_star_h, right_end_w, right_end_h))

                # 保存分割图像到指定文件夹
                img_seg_num += 1
                image_part.save(output_path + '{0}_{1}.{2}'.format(img_type, img_seg_num, suffix))
            # 分割侧边缘
            for p in range(higth_num):
                left_star_w = weight - spsize_w
                left_star_h = p * spsize_h
                right_end_w = weight
                right_end_h = left_star_h + spsize_h

                # 获得对应区域图像
                image_part = image_tiff.crop((left_star_w, left_star_h, right_end_w, right_end_h))

                # 保存分割图像到指定文件夹
                img_seg_num += 1
                image_part.save(output_path + '{0}_{1}.{2}'.format(img_type, img_seg_num, suffix))
            # 最后一个角
            left_star_w = weight - spsize_w
            left_star_h = higth - spsize_h
            right_end_w = weight
            right_end_h = higth

            # 获得对应区域图像
            image_part = image_tiff.crop((left_star_w, left_star_h, right_end_w, right_end_h))

            # 保存分割图像到指定文件夹
            img_seg_num += 1
            image_part.save(output_path + '{0}_{1}.{2}'.format(img_type, img_seg_num, suffix))
            # img_seg_num = -1
    seg_num = len(os.listdir(output_path))
    print('{0} segmentation completed'.format(img_type))
    print('A total of {0} images were segmented, resulting in {1} subgraphs'.format(len(image_list),seg_num))

# 拼接图像
def concat_images(img_path,save_path,h,w):
    size_h = h
    size_w = w
    image_files = [f for f in os.listdir(img_path) if f.startswith('test_') and f.endswith(('.png', '.jpg', '.jpeg'))]

    img_list =sorted(image_files, key=lambda x: int(os.path.splitext(x.split('_')[1])[0]))

    reconstructed_image = np.zeros((size_h, size_w, 3), dtype=np.uint8)   # 生成一个空白的图像
    h_num = size_h//512
    w_num = size_w//512

    index = 0
    for i in range(w_num):
        for j in range(h_num):
            img = cv2.imread(os.path.join(img_path, img_list[index]))  # 读取图像
            print(img_list[index])
            # 计算子块在重构图像中的位置
            y_start = j * 512
            y_end = y_start + 512
            x_start = i * 512
            x_end = x_start + 512

            # 将子块复制到重构图像的正确位置
            reconstructed_image[y_start:y_end, x_start:x_end] = img
            index+=1
    if size_h%512:
        for j in range(w_num):
            img = cv2.imread(os.path.join(img_path, img_list[index]))  # 读取图像
            # 计算子块在重构图像中的位置
            y_start = size_h - 512
            y_end = size_h
            x_start = j * 512
            x_end = x_start + 512
            # 将子块复制到重构图像的正确位置
            reconstructed_image[y_start:y_end, x_start:x_end] = img
            index += 1
    if size_w%512:
        for j in range(h_num):
            img = cv2.imread(os.path.join(img_path, img_list[index]))  # 读取图像
            # 计算子块在重构图像中的位置
            y_start = j * 512
            y_end = y_start+512
            x_start = size_w-512
            x_end = size_w
            # 将子块复制到重构图像的正确位置
            reconstructed_image[y_start:y_end, x_start:x_end] = img
            index += 1
    img = cv2.imread(os.path.join(img_path, img_list[-1]))  # 读取图像
    reconstructed_image[size_h-512:size_h, size_w-512:size_w] = img
    # 保存到文件
    save_path=os.path.join(save_path,'reconstructed_image.png')
    cv2.imwrite(save_path, reconstructed_image)

# 转换成二值图像
def exchange_label(label_path, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print('Created')
    img_list1 = os.listdir(label_path)
    img_list = sorted(img_list1, key=lambda x: int(re.search(r'\d+', x).group()))

    for img_name in tqdm(img_list):
        # img = Image.open(os.path.join(label_path, img_name))
        # # print(path)
        # w, h = img.size
        # for i in range(w):
        #     for j in range(h):
        #         if img.getpixel((i, j)) == 255:
        #              img.putpixel((i, j), 1)
        image_path = os.path.join(label_path, img_name)
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # 使用NumPy的向量化操作将255替换为1
        img[img == 255] = 1

        # 保存修改后的图片
        output_path = os.path.join(save_path, img_name)
        cv2.imwrite(output_path, img)
    # img.save(os.path.join(save_path,img_name))

def increase_data(img_path,label_path, save_data_path, save_label_path,width,height,data_type):
    image_list1 = os.listdir(img_path)
    label_list1 = os.listdir(label_path)
    label_list = sorted(label_list1, key=lambda x: int(re.search(r'\d+', x).group()))
    image_list = sorted(image_list1, key=lambda x: int(re.search(r'\d+', x).group()))
    num_pre = len(os.listdir(img_path))
    for img_name, label_name in tqdm(zip(image_list,label_list)):
        suffix_img = img_name.split('.')[-1]
        suffix_label = label_name.split('.')[-1]
        for i in range(5):
            img = Image.open(os.path.join(img_path,img_name))
            label_img = Image.open(os.path.join(label_path,label_name))
            img_new,label_new = rand_crop(img,label_img,height,width)
            img_new.save(os.path.join(save_data_path,f'{data_type}{num_pre}_{i}.{suffix_img}'))
            label_new.save(os.path.join(save_label_path, f'{data_type}_label{num_pre}_{i}.{suffix_label}'))
        num_pre +=1




"""例如：
'''Dg_train----------------------------------------------------------------------------------------------------------------'''
train_data_path = './DeepGlobe/Dg_train'
train_data_savepath = '../data_mid/Dg_train'
train_label_path = './DeepGlobe/Dg_train_label'
train_label_savepath = '../data_mid/Dg_train_label'
train_label_grey_path = '../datasets/Deepglobe/Dg_train_label'
'''Dg_test-----------------------------------------------------------------------------------------------------------------'''
test_data_path = './DeepGlobe/Dg_test'
test_data_savepath = '../data_mid/Dg_test'
test_label_path = './DeepGlobe/Dg_test_label'
test_label_savepath = '../data_mid/Dg_test_label'
test_label_grey_path = '../datasets/Deepglobe/Dg_test_label'
'''Dg_val------------------------------------------------------------------------------------------------------------------'''
val_data_path = './DeepGlobe/val_test'
val_data_savepath = '../data_mid/Dg_val_test'
val_label_path = './DeepGlobe/val_test_label'
val_label_savepath = '../data_mid/val_test_label'
val_label_grey_path = '../datasets/Deepglobe/Dg_val_label'
"""

def grey_test(img_path):
    img = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
    img[img == 1] = 255
    cv2.imshow('img_look',img)
    cv2.waitKey(0)

if __name__ == '__main__':
    image_path = 'G:/mmseg/data_lunwen/data_test'
    image_sp = 'G:/mmseg/data_lunwen/data_test'
    # img = cv2.imread('../data/ar_test/ar1.png',cv2.IMREAD_UNCHANGED)
    # h,w= img.shape[:2]
    # 分割图片
    seg_image('../data/ar_test/',image_sp,1024,1024,'png')

    # # 分割训练集
    # seg_image(image_path, image_sp, 512,512, img_type='test')
    # concat_images('../wujing_sp','../wujing_sp',h,w)

    # train_lab = '../data_mid/Dg_train_label'
    # train_save = '../datasets/DeepGlobe/Dg_train_label'
    # exchange_label(train_lab, train_save)

#分割测试集
    # seg_image(test_data_path, test_data_savepath, 256, 256, img_type='Dg_test')
    # seg_image(test_label_path, test_label_savepath, 256, 256, img_type='Dg_test_label')
    #
    # test_lab = '../data_mid/Dg_test_label'
    # test_save = '../datasets/DeepGlobe/Dg_test_label'
    # exchange_label(test_lab, test_save)

