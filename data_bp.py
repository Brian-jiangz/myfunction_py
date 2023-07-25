################################
# This is a personal information
# Establish time:2023-07-24
# Modifications time:2023-07-24
# Author:Jiang Zheng
# Email:jiangzheng@qdio.ac.cn
################################

''' The purpose of this snippet is to batch process data
from the output of HCM-AOPB'''


# 导入所需的库
## 基本库
import numpy as np 
import pandas as pd 
## 自定义函数库
import data_crb as dr # 读取二进制数据
import find_files_with_string as ffws # 查找文件
## 其他库
import glob # 读取文件夹下的文件


# 基于字典的变量赋值，包含两个字典infor和data，分别存储路径和数据集
## 定义一个字典inf，用于存储各类信息
inf = {
    "ind": {
        "ip": {
            "parent": "F:\Module\AOPB\output_FWF0\output",
        }
    }
}

## 使用ffws自定义函数读取输入文件夹下的所有dta文件名称
inf["ind"]["ip"]["filelist"] = ffws.find_files_with_string(inf["ind"]["ip"]["parent"],".dta","gct")

df = pd.DataFrame(data)
print(df.describe())
# In[]


