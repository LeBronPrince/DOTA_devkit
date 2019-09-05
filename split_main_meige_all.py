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

index_list = [1,2,3,5,7,8,9]

for index1 in index_list:
    xml_path = '/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/lable/{}/lable'.format(index1)
    txt_path = '/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/lable/{}/txt_from_xml'.format(index1)
    src_image_path = '/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/{}/{}th/Tile_1'.format(index1,index1)
    dst_image_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/JPEGImages'
    dst_label_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/labelTxt'
    anno_new_path = '/home/f523/guazai/sda/wangyang/detection/Datatemp/VOC2007/Annotations'
    src_label_path = txt_path
    images_path = dst_image_path
    labeltxt_path = dst_label_path

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
                        index = str(index1)        # the index of dataset
                        )

    split.splitdata(rate = 1)  # zoom in and out rate
    print("########## finish split ##################")

    print("########## begin dota2voc ##################")

    dota2voc(images_path, labeltxt_path, anno_new_path, ext = '.png')

    print("########## finish dota2voc ################")
