import os

def find_path_type(path):
    """
    返回一个字符串，指示给定路径的类型。

    返回值：
      'root' - 看起来像是一个 OCFL 存储根目录
      'object' - 看起来像是一个 OCFL 对象
      'file' - 一个文件，可能是一个清单文件
      其他字符串解释错误描述

    仅通过查看 "0=*" Namaste 文件来确定目录类型。
    """
    if not os.path.exists(path):
        return "路径不存在"
    
    if os.path.isfile(path):
        return "file"
    
    namaste_files = [f for f in os.listdir(path) if f.startswith("0=")]
    
    if not namaste_files:
        return "路径不包含 Namaste 文件"
    
    namaste_file = namaste_files[0]
    with open(os.path.join(path, namaste_file), 'r') as f:
        content = f.read().strip()
    
    if content == "ocfl_object_1.0":
        return "object"
    elif content == "ocfl_1.0":
        return "root"
    else:
        return "未知的 Namaste 文件内容"