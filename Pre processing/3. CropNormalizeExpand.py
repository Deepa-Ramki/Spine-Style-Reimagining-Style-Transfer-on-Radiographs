# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:47:06 2024

@author: Dharshu
"""

import os
import numpy as np
import cv2
import uuid
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("C:\\Dharshu\\College\\FYP\\Code\\PerX2CT-main\\MHD_op - Copy\\Spine_ct\\xray1.png")
plt.imshow(img, cmap = 'gray')
plt.title("Original image")

'''
Box size for DRR crop and Xray crop along with their final sizes:

#box  = left, top, right, bottom
#img_crop = img.crop((120,170,920,870)) #for xray 1000 * 1000 data
img_crop = img.crop((350,525,650,825))  #for DRR 1024*1024 data 
plt.imshow(img_crop, cmap = 'gray')
plt.title('cropped image')

w,h = img_crop.size
print(w,h)
#DRR crop size (400,350)
#xray crop size (800,700)
'''
'''
import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

#Cropping images
from os import listdir
from os.path import isfile, join
DirPath = r"C:/Dharshu/College/FYP/Data/CentralizedDataset/test_norm/";
onlyfiles = sorted_alphanumeric([f for f in listdir(DirPath) if isfile(join(DirPath, f))])
#onlyfiles.sort() did not work
#print(onlyfiles)

image_no = 1
for Img in onlyfiles:
    print(Img)
    with open(os.path.join(DirPath, Img), "rb") as file:
        BaseImg = Image.open(os.path.join(DirPath, Img))
    #with open(Img,"rb") as file: 
        #BaseImg = Image.open(Img); did not work
        print("image opened")
    #The arguments to .crop is a rect (X,Y,Width,Height)
        CroppedImg = BaseImg.crop((120,170,920,870))
        print("crop done")
        name = 'C:/Dharshu/College/FYP/Data/CentralizedDataset/X-ray cropped/file_' + str(image_no) + '.jpg'
    CroppedImg.save(name, 'JPEG')
    image_no += 1
'''
def normalize_images(dataset_path):
    # Collect pixel values of all images
    pixel_values = []
    for root, dirs, files in os.walk(dataset_path):
        for filename in files:
            if filename.endswith(".jpg"):
                image_path = os.path.join(root, filename)
                img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                pixel_values.extend(img.ravel())

    # Calculate global mean and standard deviation
    mean_val = np.mean(pixel_values)
    print(mean_val)
    std_val = np.std(pixel_values)
    print(std_val)
    
    for root, dirs, files in os.walk(dataset_path):
        for filename in files:
            if filename.endswith(".jpg"):
                image_path = os.path.join(root, filename)
                img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                
                
                normalized_img = (img - mean_val) / std_val
                
                normalized_img = (normalized_img - np.min(normalized_img)) / (np.max(normalized_img) - np.min(normalized_img)) * 255
                normalized_img = np.clip(img, 0, 255).astype(np.uint8)
                x = np.zeros((normalized_img.shape[0], normalized_img.shape[1], 3), dtype=np.uint8)
                x[:,:,0] = normalized_img  # Red channel
                x[:,:,1] = normalized_img  # Green channel
                x[:,:,2] = normalized_img  # Blue channel

                cv2.imwrite(os.path.join(save_path, filename), x)
                
dataset_path = "C:/Dharshu/College/FYP/Data/CentralizedDataset/X-ray cropped"
save_path = "C:/Dharshu/College/FYP/Data/CentralizedDataset/X-raysCN/"
normalize_images(dataset_path)
