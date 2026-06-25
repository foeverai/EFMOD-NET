import os
import cv2
from tqdm import tqdm

# 将模型预测的掩码图转换成标签图
def predic_vis(img_path, mask_path, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print('Created')
    assert os.path.exists(img_path),'no such path{0}'.format(img_path)
    assert os.path.exists(mask_path), 'no such path{0}'.format(mask_path)

    img_mask_list = os.listdir(mask_path)


    for mask_img in tqdm(img_mask_list):
        # 预测图片的名字和预测结果图片的名字是一样的
        mask_image_path = os.path.join(mask_path, mask_img)
        real_img_path = os.path.join(img_path,mask_img)
        mask = cv2.imread(mask_image_path,cv2.IMREAD_UNCHANGED)
        image = cv2.imread(real_img_path,cv2.IMREAD_UNCHANGED)

        if image is not None:
            # 使用NumPy的向量化操作将mask中对应位1的像素，在真实图片中转换成255白色，其余部分不变
            image[mask == 0] = 0
        # 保存修改后的图片
        output_path = os.path.join(save_path, mask_img)
        cv2.imwrite(output_path, image)



if __name__ == '__main__':
    image_path = 'G:/mmseg/data/Deep_Globe_1024x1024/img_dir/val'
    mask_path = 'G:/mmseg/master_paper_nudt/chapter3_bu/afdanet/afad_deep/vis'
    save_path = './predict'

    predic_vis(image_path, mask_path, save_path)




