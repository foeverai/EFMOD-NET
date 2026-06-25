import os
import re
from PIL import Image

# # 获取大图像的宽度和高度
# combined_width, combined_height = combined_img.size

# # 假设你知道原来两张小图像的宽度（或者可以通过某种方式计算出来）
# # 这里我们假设它们分别是width1和width2，并且width1 + width2 = combined_width
# width1, width2 = 512,512  # 示例宽度，你需要替换为实际的宽度值
#
# # 根据宽度切割大图像以获取原来的两张小图像
# img1 = combined_img.crop((0, 0, width1, combined_height))
# img2 = combined_img.crop((width1, 0, combined_width, combined_height))
#
# # 显示或保存切割后的小图像
# img1.show()  # 显示第一张小图像
# img2.show()  # 显示第二张小图像
#
# # 或者
# img1.save('./test_data/img1.jpg')  # 保存第一张小图像
# img2.save('./test_data/img2.jpg')  # 保存第二张小图像


def cat_img(file_path1:str,file_path2:str,save_path:str) ->str:
    # 确保图像路径存在
    assert os.path.exists(file_path1), "The file path1 of images is not exist！"
    assert os.path.exists(file_path2), "The file path2 of images is not exist！"
    img_list1 = os.listdir(file_path1)
    img_list2 = os.listdir(file_path2)

    img_list1=sorted(img_list1, key=lambda x: int(re.search(r'\d+', x).group()))
    img_list2=sorted(img_list2, key=lambda x: int(re.search(r'\d+', x).group()))

    for i in range(len(img_list1)):
        img1 = Image.open(os.path.join(file_path1,img_list1[i]))    # 打开图像文件
        img2 = Image.open(os.path.join(file_path2,img_list2[i]))    # 打开需要拼接的图像
        # 确保两张图像的高度是相同的
        assert img1.height == img2.height, "Images must have the same height to be concatenated horizontally."

        # 计算拼接后的新宽度
        new_width = img1.width + img2.width

        # 创建一个新的空白图像，其大小为两张图像的高度和新的宽度
        combined_img = Image.new('RGB', (new_width, img1.height))

        # 将第一张图像粘贴到新的空白图像的左侧
        combined_img.paste(img1, (0, 0))

        # 将第二张图像粘贴到新的空白图像的右侧
        combined_img.paste(img2, (img1.width, 0))

        # 保存图像
        save_name = f'{save_path}/train{i}.png'
        combined_img.save(save_name)  # 保存图像

        return save_path

