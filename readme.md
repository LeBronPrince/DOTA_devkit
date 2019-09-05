1. sudo ./install.sh
    进行相关编译。python3.5 和 3.7 我都试过未出现编译错误。如果编译出错，可以放弃编译。单独切图不太需要这个编译。

2. 安装相应未安装的库。

3. 切割思路：
    (1) 将xml标签格式转为 DOTA 数据集的txt标签格式（程序是根据Dota官方的程序改的）。
    (2) 将图片和相应生产的 txt 文件进行切割。
    (3) 再将切割后的 txt 格式标签转为为VOC格式的XML标签。
    (4) 将VOC格式的XML便签转化为 YOLO 格式的标签。  (程序未实现)
    注：只实现了(1),(2),(3)步骤。

4. 程序的使用：
    (1) 3(1) 对应程序 xml2txt.py:
        需要更改的参数:
            xml_path: xml标签保存的文件夹
            txt_path: txt标签保存的文件夹
        结果：在 txt_path 文件夹生产 TXT 标签

    (2) 3(2) 对应程序 split_main1.py
        需要更改参数：
            src_image_path： 原始大图存储路径
            src_label_path： TXT 标签的路径
            dst_image_path： 切割成的小图要存储的路径
            dst_label_path： 切割成的 TXT 标签存储路径
            gap ：重叠尺寸
            subsize ：子图大小
            thresh ：如果一个标签被切割，那么当切割比例大于 thresh 的时候，才保存； 否则舍弃。
            ext ：图片扩展名字 png
            index : 代表数据是第几条数据。因为8条数据里的图片名字都是 Result_xxx.png，
                    为了防止将八条数据拷贝到一起的时候，出现覆盖错误，把index加入文件名字中。

    (3) 3(3) 对应程序 dota2voc.py
        需要更改的参数：
            images_path ：切割后小图的存储路径
            labeltxt_path ：切割后TXT标签的存储路径
            anno_new_path ：生产的 XML 保存路径。
            ext ：图片的拓展名 (.png)。

5. 使用步骤：
    对于每条数据集，先运行 xml2txt.py； 再运行split_main1.py; 最后运行dota2voc.py
    注意 更改步骤 4 步骤中介绍的相关文件路径和存储路径。

6. 聚合版本：
    split_main_merge_all.py包括了所有三个步骤
    需要更改的参数：
        xml_path ：XML标签保存的文件夹txt_path
        txt_path ：生成的TXT标签保存的文件夹 (未进行切割)
        src_image_path ：原始图片文件夹
        ***dst_image_path ：切割后子图片保存文件夹***
        dst_label_path ：切割后标签文件TXT标签保存文件夹
        ***anno_new_path ： 切割后TXT标签转化的VOC格式的XML文件保存文件夹***
    注 ：通过整体迭代实现一次性切割。
