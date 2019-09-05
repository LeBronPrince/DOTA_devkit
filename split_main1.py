# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import os
from DOTA import DOTA
import dota_utils as util
import pylab
from ImgSplit1 import splitbase

# source image path
src_image_path = '/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/9/9th/Tile_1'
# source label path
src_label_path = '/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/lable/9/txt_from_xml'

# save image path
dst_image_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/JPEGImages'
# save label path
dst_label_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/labelTxt'


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
