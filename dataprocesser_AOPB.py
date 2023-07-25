################################
# This is a personal information
# Establish time:2023-05-07
# Modifications time:2023-07-25
# Author:Jiang Zheng
# Email:jiangzheng@qdio.ac.cn
################################

''' The purpose of this snippet is to read the binary data from
the output of HCM-AOPB'''


import numpy as np


class dataprocesser_AOPB:
   def __init__(self,data,info):
      self.info = info
      self.data = data
      
      
   def data_rb(filename):
      # 读取二进制文件 
      
      # 输入参数：
      # filename:数据的路径
      
      # 输出参数：
      # data:读取的数据
      
      
      data = np.fromfile(filename, dtype=np.float32)
      return data
   
   def data
# In[ ]:

