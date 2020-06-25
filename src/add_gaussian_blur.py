import cv2
import os
import numpy as np
from tqdm import tqdm

os.makedirs('../input/gaussian_blurred', exist_ok = True)
src_dir = '../input/sharp'
images = os.listdir(src_dir)
dst_dir = '../input/gaussian_blurred'

for i, img in tqdm(enumerate(images), total = len(images)):
    img = cv2.imread(f"{src_dir}/{images[i]}", cv2.IMREAD_COLOR)
    blur = cv2.GaussianBlur(img, (31, 31), 0) # Kernel size (31, 31)
    cv2.imwrite(f"{dst_dir}/{images[i]}", blur)
print("Completed Blurring!")