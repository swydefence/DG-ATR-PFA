import os
import numpy as np
import cv2

def process_image(image_path):
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"图像读取失败，请检查路径: {image_path}")

    # 将图像转换为float32类型以提高精度
    image_float = image.astype(np.float32)

    # 将图像转换为分贝（dB）
    log_image = 20 * np.log1p(image_float)

    # 将log图像归一化到[0, 255]范围
    log_image_normalized = cv2.normalize(log_image, None, 0, 255, cv2.NORM_MINMAX)

    # 转换回uint8类型
    log_image_normalized = log_image_normalized.astype(np.uint8)

    # 保存处理后的图像，替换原图像
    cv2.imwrite(image_path, log_image_normalized)

def process_images_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                image_path = os.path.join(root, file)
                try:
                    process_image(image_path)
                except ValueError as e:
                    print(e)

# 示例调用
process_images_in_directory('')