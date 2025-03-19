import os
import cv2
import numpy as np
import random


def add_gaussian_noise(image, mean=0, std=255):
    h, w = image.shape
    noise = np.random.normal(mean, std, (h, w))
    noisy_image = image + random.uniform(0.2, 0.6)*noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def process_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                noisy_image = add_gaussian_noise(image)
                cv2.imwrite(image_path, noisy_image)
                

# 指定文件夹路径
folder_path = "data\sample\/trans"

# 处理图像
process_images(folder_path)