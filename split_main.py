# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import os
from DOTA import DOTA
import dota_utils as util
import pylab
from ImgSplit import splitbase

#/home/f523/guazai/sda/dota/train
#/home/f523/guazai/sda/dota/dota_voc/VOC2007
path = '/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/9/9th'
path1 = '/home/f523/guazai/sda/wangyang/detection/Data8/VOC2007'
split = splitbase(path,path1, choosebestpoint=True)
split.splitdata(1)
