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
    import os

    if not os.path.exists(path):
        return "路径不存在"

    namaste_file = os.path.join(path, "0=*")
    
    if os.path.isdir(path) and os.path.isfile(namaste_file):
        with open(namaste_file, 'r') as file:
            content = file.read().strip()
            if content == "OCFL Root":
                return "root"
            elif content.startswith("OCFL Object"):
                return "object"
            elif content.startswith("Manifest File"):
                return "file"
            else:
                return "未知类型"
    elif os.path.isfile(path):
        return "file"
    else:
        return "未知类型"