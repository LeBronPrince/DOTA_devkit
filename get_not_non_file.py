import os
import xml.etree.ElementTree as ET
import cv2

data_path = "/home/f523/guazai/sda/wangyang/detection/Data1/VOC2007/Annotations"
save_path = "/home/f523/guazai/sda/wangyang/detection/Data1/VOC2007/ImageSets/Main/train.txt"

file_txt = open(save_path,"w")

files = os.listdir(data_path)
for file1 in files:
    path = os.path.join(data_path,file1)
    tree = ET.parse(path)
    root = tree.getroot()
    obj = root.find('object')
    if obj is not None:
        file_txt.write(file1[:-4]+"\n")
    else:
        print(file1[:-4])
