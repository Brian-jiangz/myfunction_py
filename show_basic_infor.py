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

def show_basic_infor(data,info):
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
    data_raw = data["raw"]["dataset"]
    
    # 获取变量的基本信息
    if not isinstance(data["raw"]["dataset"], np.ndarray):
        data_2d = np.array(data["raw"]["dataset"])
    else:
            data_2d = data["raw"]["dataset"]
            
    # 获取变量的维度
    data_shape = data_2d.shape
    data_frame = np.transpose(data_2d)
        
    # dataframe转化
    data_frame = pd.DataFrame(data_frame,columns=[f"Time {i+1}" for i in data_frame[0]])
        
    # 统计信息
    statistics = data_frame.describe()
    
    # 绘制统计图表
    ## 绘制空缺值图像
    plt.figure(figsize=(8,6))
    sns.heatmap(data_frame.isnull(),cbar=False,cmap='viridis')
    plt.title('Missing values in the data')
    plt.show()
    
    ## 绘制一个时间点的数据分布图像
    plt.figure(figsize=(8,6))
    x=np.array(0,91)
    y=np.array(0,161)
    X,Y = np.meshgrid(x,y)
    plt.contour(X,Y,data)