################################
# This is a personal information
# Establish time:2023-07-24
# Modifications time:2023-07-24
# Author:Jiang Zheng
# Email:jiangzheng@qdio.ac.cn
################################

''' The purpose of this snippet is to find dta files from a folder with special string'''
import os # 用于操作文件路径
import glob # 读取文件夹下的文件

def find_files_with_string(folder_path, file_extension, search_string):
    """
    在指定文件夹内搜索包含特定字符串的文件名，并返回符合条件的文件名列表。

    参数:
    folder_path (str): 文件夹路径。
    file_extension (str): 文件扩展名，例如 ".dta"。
    search_string (str): 要搜索的字符串。

    返回:
    list: 符合条件的文件名列表。
    """
    # 构造要搜索的文件路径模式
    search_pattern = os.path.join(folder_path, f"*{search_string}*{file_extension}")

    # 使用 glob 模块获取符合条件的文件路径列表
    matched_files = glob.glob(search_pattern)

    # 从文件路径中提取文件名，并返回文件名列表
    file_names = [os.path.basename(file_path) for file_path in matched_files]
    return file_names
