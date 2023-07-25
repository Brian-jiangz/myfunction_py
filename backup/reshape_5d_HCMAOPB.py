################################
# This is a personal information
# Establish time:2023-07-25
# Modifications time:2023-07-25
# Author:Jiang Zheng
# Email:jiangzheng@qdio.ac.cn
################################

''' The purpose of this snippet is to reshape output data of HCMAOPB model to initial 5 dimention'''

def reshape_5d_HCMAOPB(data,info):
    # 将HCM-AOPB输出的数据还原成为5维
    
    # 输入参数：
    # data:HCM-AOPB的原始输出变量
    
    # 输出参数：
    # data_5d:还原后的5维变量
    
    
    data_5d = data.reshape((info["lon"],info["lat"],info["year"],info["mon"],info["day"]),order='F')
    return data_5d