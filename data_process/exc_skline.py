import cv2
import os
import numpy as np
from tqdm import tqdm
from PIL import Image
from label_to_mask import exchange_predic

# 提取中心线
def exter_Skeleton(image,save_path):
    """
    提取二值图像的中心线
    :param image_path:图片路径
    :param save_path: 图片保存路径
    :return: 图片保存路径
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # # # 读取二值图像
    # img = cv2.imread(image_path, 0)
    img = image

    # 使用OpenCV的细化算法进行中心线提取
    skeleton = np.zeros_like(img)

    skeleton = cv2.ximgproc.thinning(img, skeleton)

    # 保存结果
    save_name = os.path.join(save_path,'skeline.png')
    cv2.imwrite(save_name, skeleton)  # 指定保存路径和文件名

    return save_name


# 扩充图像
def pad_image(image_path,save_pad,pad_size=3):
    """
    填充边界
    :param image_path:图片路径
    :param save_pad: 扩充图片保存位置
    :param pad_size: 扩充边界的像素值
    :return: 扩充后像素矩阵和保存路径
    """
    if not os.path.exists(save_pad):
        os.makedirs(save_pad)

    img_list = os.listdir(image_path)
    for image_name in tqdm(img_list):
        img_path = os.path.join(image_path, image_name)
        img = Image.open(img_path)

        # 获取原始尺寸
        original_width, original_height = img.size

        # 计算新的宽度和高度
        new_width = original_width + pad_size
        new_height = original_height + pad_size

        # 创建一个新的黑色背景图像（或选择其他颜色）
        padded_img = Image.new(img.mode, (new_width, new_height), "black")

        # 将原始图像粘贴到新图像的中心
        padded_img.paste(img, ((new_width - original_width) // 2, (new_height - original_height) // 2))
        output_path = os.path.join(save_pad, image_name)

        padded_img.save(output_path)

# 恢复原来的尺寸
def re_img(image_path,restore_dir,pad_size=3):
    """
    去除周围添加的像素
    Args:
        image_path: 图像文件所在位置
        restore_dir: 恢复后的图片存放位置
        pad_size:添加的像素长度
    Returns:None

    """
    if not os.path.exists(restore_dir):
        os.makedirs(restore_dir)

    img_list = os.listdir(image_path)
    for image_name in tqdm(img_list):
        img_path = os.path.join(image_path, image_name)
        img = Image.open(img_path)

        # 获取原始尺寸
        padded_width, padded_height = img.size

        # 计算新的宽度和高度
        original_width = padded_width - pad_size
        original_height = padded_height - pad_size
        left = pad_size // 2
        top = pad_size // 2
        right = left + original_width
        bottom = top + original_height

        # 裁剪图像
        restored_img = img.crop((left, top, right, bottom))

        # 保存恢复后的图像
        output_path = os.path.join(restore_dir, image_name)
        restored_img.save(output_path)


def exter_Skeleton_for_file(image_dir,save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    image_list = os.listdir(image_dir)
    for image_name in tqdm(image_list):
        image_path = os.path.join(image_dir,image_name)
        image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

        skeleton = np.zeros_like(image)
        skeleton = cv2.ximgproc.thinning(image, skeleton)
        # 保存结果
        save_name = os.path.join(save_dir,image_name)
        cv2.imwrite(save_name, skeleton)  # 保存路径

if __name__ == '__main__':
    image_path = "G:/mmseg/data/Deep_Globe_skline/ann_dir/train_vis"
    save_pad = "G:/mmseg/data/Deep_Globe_skline/ann_dir/train_pad"
    save_sk_path = "G:/mmseg/data/Deep_Globe_skline/ann_dir/train_sk"
    save_re_path = "G:/mmseg/data/Deep_Globe_skline/ann_dir/train_re_sk"

    # pad_image(image_path,save_pad)

    # exchange_predic(image_path, save_path)
    # exter_Skeleton_for_file(save_pad,save_sk_path)
    re_img(save_sk_path,save_re_path,pad_size=3)








