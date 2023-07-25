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
import pandas as pd
import glob # 读取文件夹下的文件
import os # 用于操作文件路径


class dataprocesser_AOPB:
   def __init__(self,data,info):
      self.info = info
      self.data = data
      
      
   def data_rb(info):
      # 读取二进制文件 
      
      # 输入参数：
      # info:包含数据信息的字典，使用其中的cont(计数器)和fileslist(文件列表)，以读取文件路径
      
      # 输出参数：
      # data:读取的数据
      
      filename = info["ind"]["ip"]["filepath"]
      data_tem = np.fromfile(filename, dtype=np.float32)
      return data_tem
   
   def reshape_5d_HCMAOPB(data,info):
      # 将HCM-AOPB输出的数据还原成为5维
      
      # 输入参数：
      # data:HCM-AOPB的原始输出变量
      # info:包含数据信息的字典
      
      # 输出参数：
      # data_5d:还原后的5维变量
      
      data_tem = data["raw"]["dataset"]
      info_dim = info["data"]["raw"]["dim"]
      data["raw"]["dataset_5d"] = data_tem.reshape((info_dim["lon"],info_dim["lat"],info_dim["year"],info_dim["mon"],info_dim["day"]),order='F')
      return data
   
   
   def find_files_with_string(info):
      """
      在指定文件夹内搜索包含特定字符串的文件名，并返回符合条件的文件名列表。

      参数:
      info: 存储数据信息的字典，使用其中的["Var"]，以读取变量信息
         folder_path (str): 文件夹路径。
         file_extension (str): 文件扩展名，例如 ".dta"。
         search_string (str): 要搜索的字符串。

      返回:
      list: 符合条件的文件名列表。
      """
      # 变量赋值
      folder_path = info["ind"]["ip"]["parent"]
      file_extension = info["var"]["file"]["extension"]
      search_string = info["var"]["datanow"]["search_string"]
      
      # 构造要搜索的文件路径模式
      search_pattern = os.path.join(folder_path, f"*{search_string}*{file_extension}")

      # 使用 glob 模块获取符合条件的文件路径列表
      matched_files = glob.glob(search_pattern)

      # 从文件路径中提取文件名，并返回文件名列表
      file_names = [os.path.basename(file_path) for file_path in matched_files]
      info["ind"]["ip"]["fileslist"] = file_names
      return info
# In[ ]:

