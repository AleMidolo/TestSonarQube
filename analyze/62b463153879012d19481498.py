def files_list(path):
    """
    返回给定路径中的文件。
    返回 `path` 中的文件。
    """
    import os
    
    # 获取路径下所有文件和目录
    files = os.listdir(path)
    
    # 过滤出文件,排除目录
    files = [f for f in files if os.path.isfile(os.path.join(path, f))]
    
    return files