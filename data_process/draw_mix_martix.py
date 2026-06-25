import os

import cv2
import numpy as np
from tqdm import tqdm


def visualize_predictions(pred_image, gt_image):
    """
    输入：
    - pred_image: 预测图，单通道灰度图像，道路为255，背景为0。
    - gt_image: 标签图（Ground Truth），单通道灰度图像，道路为255，背景为0。

    输出：
    - result_image: 可视化结果，真阳性为白色，假阳性为绿色，假阴性为红色。
    """
    # 确保输入图像是单通道灰度图像
    if len(pred_image.shape) > 2:
        pred_image = cv2.cvtColor(pred_image, cv2.COLOR_BGR2GRAY)
    if len(gt_image.shape) > 2:
        gt_image = cv2.cvtColor(gt_image, cv2.COLOR_BGR2GRAY)

    # 初始化结果图像，黑色背景
    result_image = np.zeros((pred_image.shape[0], pred_image.shape[1], 3), dtype=np.uint8)

    # 计算真阳性（TP）：预测为道路且标签也为道路
    tp = (pred_image == 255) & (gt_image == 255)
    result_image[tp] = [255, 255, 255]  # 白色

    # 计算假阳性（FP）：预测为道路但标签为背景
    fp = (pred_image == 255) & (gt_image == 0)
    result_image[fp] = [0, 255, 0]  # 绿色

    # 计算假阴性（FN）：预测为背景但标签为道路
    fn = (pred_image == 0) & (gt_image == 255)
    result_image[fn] = [0, 0, 255]  # 红色

    return result_image


def visualize_predictions_dir(pred_image_path,gt_image_path,save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    pre_img_list = os.listdir(pred_image_path)
    gt_img_list = os.listdir(gt_image_path)

    for pre_img, gt_img in tqdm(zip(pre_img_list, gt_img_list), desc="处理进度", unit="张"):
        img = cv2.imread(os.path.join(pred_image_path, pre_img))
        gt = cv2.imread(os.path.join(gt_image_path, gt_img))
        mix_img = visualize_predictions(img, gt)
        cv2.imwrite(os.path.join(save_path, pre_img), mix_img)

    print("任务执行完成！")

# 示例用法
if __name__ == "__main__":
    pre_path = r"G:\mmseg\master_paper_nudt\chapter3_bu\afdanet\afad_deep\vis_pre"
    gt_path = r"G:\mmseg\data\Deep_Globe_1024x1024\ann_dir\val_vis"
    save_path = r"G:\mmseg\master_paper_nudt\chapter3_bu\afdanet\afad_deep\vis_result"
    visualize_predictions_dir(pre_path, gt_path, save_path)




    # # 读取预测图和标签图
    # pred_image_path = "./test_data/sh100854_sat.png"  # 替换为预测图路径
    # gt_image_path = "./predict/"  # 替换为标签图路径
    #
    # pred_image = cv2.imread(pred_image_path, cv2.IMREAD_GRAYSCALE)
    # gt_image = cv2.imread(gt_image_path, cv2.IMREAD_GRAYSCALE)
    #
    # # 生成可视化结果
    # result_image = visualize_predictions(pred_image, gt_image)
