
# coding: utf-8

# # Usage for parse ground truth file and show
# This is a demo for parse, visulize and split the data, the demo use the data in example folder,
# but the folder does not neccessaryly include all the categories.

# In[1]:

#get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
import os
from DOTA import DOTA
import dota_utils as util
import pylab
pylab.rcParams['figure.figsize'] = (20.0, 20.0)


# In[2]:

example = DOTA('example')


# In[3]:

imgids = example.getImgIds(catNms=['ship', 'storage-tank'])
imgid = imgids[0]
img = example.loadImgs(imgid)[0]


# In[4]:

plt.axis('off')

plt.imshow(img)
plt.show()


# In[17]:

anns = example.loadAnns(imgId=imgid)
# print(anns)
example.showAnns(anns, imgid, 2)


# ## Split Image And Label
# We provide the scale param before split the images and labels.
# Sometimes, the instance is too large that it can be easily cut down(for example, ground track filed), in such case you need to set the param "rate" less than 1.
#
# Before going on, first create folder to store the split data
# ```
#   mkdir examplesplit
#   mkdir examplesplit/images
#   mkdir examplesplit/labelTxt
# ```
# For test images, you only need to split images, refer to "SplitOnlyImage.py"

# In[5]:

from ImgSplit import splitbase


# In[6]:

split = splitbase(r'example',
                 r'examplesplit', choosebestpoint=True)
split.splitdata(0.5)
split.splitdata(1)
split.splitdata(2)


# In[7]:

examplesplit = DOTA('examplesplit')


# In[8]:

imgids = examplesplit.getImgIds(catNms=['plane'])
imgid = imgids[1]
img = examplesplit.loadImgs(imgid)[0]


# In[9]:

plt.axis('off')

plt.imshow(img)
plt.show()


# In[10]:

anns = examplesplit.loadAnns(imgId=imgid)
# print(anns)
examplesplit.showAnns(anns, imgid, 2)


# ## Merge patches
# Now, we will merge these patches to see if they can be restored in the initial large images

# In[11]:

from ResultMerge import mergebypoly


# In[12]:

util.groundtruth2Task1(r'examplesplit/labelTxt',
                      r'Task1')
mergebypoly(r'Task1',
           r'Task1_merge')
util.Task2groundtruth_poly(r'Task1_merge',
                          r'restoredexample/labelTxt')


# In[13]:

filepath = 'example/labelTxt'
imgids = util.GetFileFromThisRootDir(filepath)
imgids = [util.custombasename(x) for x in imgids]
print(imgids)


# In[14]:

example = DOTA(r'example')
num = 2
anns = example.loadAnns(imgId=imgids[num])
# print(anns)
example.showAnns(anns, imgids[num], 2)


# In[15]:

restored = DOTA(r'restoredexample')
num = 2
anns = restored.loadAnns(imgId=imgids[num])
# print(anns)
restored.showAnns(anns, imgids[num], 2)
