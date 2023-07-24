################################
# This is a personal information
# Establish time:2023-05-07
# Modifications time:2023-05-07
# Author:Jiang Zheng
# Email:jiangzheng@qdio.ac.cn
################################

''' The purpose of this snippet is to read the binary data from
the output of HCM-AOPB'''


import numpy as np


def data_rb(filename):
    '''
    11
    Args:
       11
    Returns:
       11
    '''
    data = np.fromfile(filename, dtype=np.float32)
    return data
# In[ ]:
