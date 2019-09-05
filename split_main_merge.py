# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import os
from DOTA import DOTA
import dota_utils as util
import pylab
from ImgSplit1 import splitbase
from xml2txt_merge import xml2txt
from dota2voc_merge import dota2voc
"""
index_list = [1,2,3,5,7,8,9]
for index1 in index_list:
    xml_path =
    txt_path =
    src_image_path =
    dst_image_path =
    dst_label_path =
    anno_new_path = 
"""
###################################
# source xml path
xml_path = "/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/lable/9/lable"

# save txt path
txt_path = "/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/lable/9/txt_from_xml"
###################################


##################################
# source image path
src_image_path = '/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/9/9th/Tile_1'
# source label path
src_label_path = txt_path

# save image path
dst_image_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/JPEGImages'
# save label path
dst_label_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/labelTxt'

##################################

#################################
images_path = dst_image_path # 样本图片路径
labeltxt_path = dst_label_path # DOTA标签的所在路径
anno_new_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/Annotations'  # 新的voc格式存储位置（hbb形式）
################################
print("########### begin xml2txt #############")
xml2txt(xml_path,txt_path)
print("########### finish xml2txt #############")

print("########### begin split #################")
split = splitbase(  src_image_path,
                    src_label_path,
                    dst_image_path,
                    dst_label_path,
                    gap = 300,                 # overlapping
                    subsize = 1024,            # sub image size
                    thresh = 0.3,              # min label area rate
                    choosebestpoint = True,
                    ext = '.png',              # image format
                    index = '9'                # the index of dataset
                    )
split.splitdata(rate = 1)  # zoom in and out rate
print("########## finish split ##################")

print("########## begin dota2voc ##################")

dota2voc(images_path, labeltxt_path, anno_new_path, ext = '.png')

print("########## finish dota2voc ################")
