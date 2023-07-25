################################
# This is a personal information
# Establish time:2023-07-24
# Modifications time:2023-07-24
# Author:Jiang Zheng
# Email:jiangzheng@qdio.ac.cn
################################

import data_rb as data_rb
import pandas as pd
''' The purpose of this snippet is to merge a 3-dimensional data set from multiple dta files in a files list'''
def merge_data_from_files(dta_files):
    """
    合并多个dta文件中的数据，并按时间顺序构造三维新数据。

    参数:
    folder_path (str): 文件夹路径。
    file_extension (str): 文件扩展名，例如 ".dta"。
    search_string (str): 要搜索的字符串。

    返回:
    numpy.ndarray: 三维新数据，第一维和第二维是经纬度，第三维是时间序列。
    """
    # 初始化空的DataFrame用于合并数据
    merged_df = pd.DataFrame()

    # 循环读取每个dta文件，并将其合并到merged_df中
    for file_path in dta_files:
        df = data_rb.data_rb(file_path)
        merged_df = pd.concat([merged_df, df])

    # 将数据按时间顺序排序并转换为三维新数据
    merged_df.sort_values(by="时间序列", inplace=True)
    num_time_steps = len(merged_df["时间序列"].unique())
    num_latitudes = len(merged_df["纬度"].unique())
    num_longitudes = len(merged_df["经度"].unique())
    merged_data = merged_df["数据值"].values.reshape(num_time_steps, num_latitudes, num_longitudes)

    return merged_data