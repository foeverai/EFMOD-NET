import os.path

from PIL import Image
import numpy as np
import math
from tqdm import tqdm


def is_power_of_two(n):
    return (n & (n - 1)) == 0



def resize_img(img_path,save_path):
    """
    调整图像的尺寸，检查图像的长宽尺寸是否是2的幂次方，如果不是则使用0将其进行边界填充
    Args:
        img_path:图像所在文件夹目录
        save_path:图像的保存目录

    Returns:

    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    img_list = os.listdir(img_path)
    for image in tqdm(img_list):
        img_open = Image.open(os.path.join(img_path,image))
        width, height = img_open.size
        # 检查长宽是否是2的幂次方,如果是则返回，否则进行pad的填充
        if is_power_of_two(width) and is_power_of_two(height):
            print(f"Image size {width}x{height} is already a power of two. No padding needed.")
            img_open.save(os.path.join(save_path, image))
            continue

            # 计算新的宽度和高度，使其为2的幂次方
        new_width = 2 ** math.ceil(math.log2(width))
        new_height = 2 ** math.ceil(math.log2(height))

        # 创建一个新的空白图片，用于填充
        new_img = Image.new(img_open.mode, (new_width, new_height), color=0)  # 使用0填充

        # 将原始图片粘贴到新图片的中心位置
        new_img.paste(img_open, ((new_width - width) // 2, (new_height - height) // 2))

        # 保存新图片
        new_img.save(os.path.join(save_path, image))
    print(f"Image has been padded to size {new_width}x{new_height}")

def pad_image_custom(image_path,save_path,pad_size:list):
    """
    自定义扩展的图像尺寸
    Args:
        image_path:原始图像的路径
        save_path: 扩展之后图像的保存路径
        pad_size: 扩展之后的图像尺寸

    Returns:None

    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    img_list = os.listdir(image_path)
    for img in tqdm(img_list):
        img_open = Image.open(os.path.join(image_path,img))
        # 获取原始图像的宽高
        w,h = img_open.size
        # 计算扩展之后的宽高
        new_w = w+pad_size[0]
        new_h = h+pad_size[1]
        # 创建一个新的空白图像，用于填充
        new_img = Image.new(img_open.mode, (new_w, new_h), color=0)  # 使用0填充

        # 将原始图像粘贴到新图片的位置
        left = (new_w - w) // 2
        top = (new_h - h) // 2
        new_img.paste(img_open, (left, top))

        # 保存新图片
        new_img.save(os.path.join(save_path, img))
        # print(f"Image has been padded to size {new_w}x{new_h}")
    print("All images have been padded.")


# 使用示例
# input_image_path = 'Image_01L.png'  # 替换为你的图片路径
# output_image_path = 'Image_01Lg.jpg'  # 替换为你想要保存的路径
# pad_to_power_of_two(input_image_path, output_image_path)
if __name__ == '__main__':
    image_path = r'../data/CHASE_DB1/img_dir/validation'
    label_path = r'../data/CHASE_DB1/annotations/validation'

    image_save = r'../data/CHASE_DB1_pad/img_dir/validation'
    label_save = r'../data/CHASE_DB1_pad/annotations/validation'

    resize_img(image_path,image_save)

    # pad_image_custom(image_path,image_save,[36,36])
    # pad_image_custom(label_path,label_save,[36,36])


