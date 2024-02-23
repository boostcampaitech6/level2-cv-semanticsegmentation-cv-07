import os
import cv2
from PIL import Image
from shutil import copytree

dir_path = "../data/train/DCM"  # 바꾸려는 디렉토리 경로를 지정합니다.

for dir_name in os.listdir(dir_path):
    if dir_name.startswith("ID0"):
        original_dir = os.path.join(dir_path, dir_name)
        new_dir = os.path.join(dir_path, "ID1" + dir_name[3:])
        copytree(original_dir, new_dir)  # 디렉토리를 복사합니다.

        # 복사된 디렉토리의 이미지를 좌우 반전시킵니다.
        for file_name in os.listdir(new_dir):
            if file_name.startswith("image"):
                img_path = os.path.join(new_dir, file_name)
                img = Image.open(img_path)
                img = img.transpose(Image.FLIP_LEFT_RIGHT)  # 이미지를 좌우 반전시킵니다.
                img.save(img_path)  # 이미지를 저장합니다.
