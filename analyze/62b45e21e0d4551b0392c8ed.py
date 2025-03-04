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
    import glob

    # 检查路径是否存在
    if not os.path.exists(path):
        return "Path does not exist"

    # 如果是文件
    if os.path.isfile(path):
        return "file"

    # 如果是目录，查找 0=* 文件
    if os.path.isdir(path):
        namaste_files = glob.glob(os.path.join(path, "0=*"))
        
        if not namaste_files:
            return "No Namaste files found"
            
        # 读取第一个找到的 0=* 文件内容
        try:
            with open(namaste_files[0], 'r') as f:
                content = f.read().strip()
                
            # 检查内容判断类型
            if "ocfl_" in content.lower():
                if "object" in content.lower():
                    return "object"
                elif "root" in content.lower():
                    return "root"
                    
            return f"Unknown Namaste content: {content}"
            
        except Exception as e:
            return f"Error reading Namaste file: {str(e)}"
            
    return "Unknown path type"