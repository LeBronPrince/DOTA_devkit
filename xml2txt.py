'''
transfer xml label to DOTA txt label format
'''

import os
import xml.etree.ElementTree as ET
import cv2

# source xml path
xml_path = "/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/lable/9/lable"

# save txt path
txt_path = "/home/f523/guazai/sda/wangyang/detection/遥感比赛测试数据/lable/9/txt_from_xml"


if not os.path.exists(txt_path):
    os.mkdir(txt_path)

for root,dirs,files in os.walk(xml_path):
    num = len(files)
    print('total num is %d' %(num))
    for file in files:
        name = os.path.join(xml_path,file)
        tree = ET.parse(name)
        root = tree.getroot()
        obj = root.findall('object')
        f = open(os.path.join(txt_path, file[:-4] + '.txt'), 'w')
        #f.write("imagesource:GoogleEarth"+'\n')
        #f.write("gsd:0.115726939386"+'\n')
        for obj1 in obj:
            label = obj1.find('name').text
            x1 = obj1.find('bndbox').find('xmin').text
            y1 = obj1.find('bndbox').find('ymin').text
            x2 = obj1.find('bndbox').find('xmax').text
            y2 = obj1.find('bndbox').find('ymin').text
            x3 = obj1.find('bndbox').find('xmax').text
            y3 = obj1.find('bndbox').find('ymax').text
            x4 = obj1.find('bndbox').find('xmin').text
            y4 = obj1.find('bndbox').find('ymax').text
            f.write(str(x1)+ ' '+str(y1)+ ' '+str(x2)+ ' '+str(y2)+ ' '+str(x3)+ ' ' +str(y3)+ ' '+str(x4)+ ' '+str(y4)+ ' '+label+' '+str(0)+'\n')
        f.close()
