################################
# This is a personal information
# Establish time:2023-07-25
# Modifications time:2023-07-25
# Author:Jiang Zheng
# Email:jiangzheng@qdio.ac.cn
################################

''' The purpose of this snippet is to show the basic information of a variable'''

    # 引用包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

def show_basic_infor(data):
    # 自定义函数，输入变量，通过函数输出变量的基本信息，并以统计图象和表格的形式输出
    
    # 输入参数：
    # data：变量（字典）
    
    # 输出参数：
    # data_dim:变量的维度
    # data_shape:变量的形状
    # data_type:变量的数据类型
    # data_size:变量的大小
    # data_maxmin:变量的最大最小值
    # data_mean:变量的平均值
    # data_std:变量的标准差
    # data_var:变量的方差
    # data_null:变量的空值
    
    # 分配变量
    
    # 获取变量的基本信息
    if not isinstance(merge_data_3d, np.ndarray):
            merge_data_3d = np.array(merge_data_3d)
            
    # 获取变量的维度
    data_shape = merge_data_3d.shape
    data_frame = np.transpose(merge_data_3d)
        
    # dataframe转化
    data_frame = pd.DataFrame(data_frame,columns=[f"Time {i+1}" for i in data_frame[0]])
        
    # 统计信息
    statistics = data_frame.describe()
    
    # 绘制统计图表
    ## 绘制空缺值图像
    plt.figure(figsize=(8,6))
    sns.heatmap(data_frame.isnull(),cbar=False,cmap='viridis')