import os

def is_file_exist(file_name):
    """
    检查 file_name 是否是一个已存在的文件。
    检查文件名是否存在。

    :param file_name: 文件名。
    :type file_name: str
    :return: 如果存在，则返回真，如果不存在或是无效的文件名则返回假。
    :rtype: bool
    """
    return os.path.isfile(file_name)