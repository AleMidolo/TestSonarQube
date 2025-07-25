def match_file_by_prefix(prefix, file_path):
    """
    根据给定的文件路径，如果文件路径的文件名以指定的前缀加上"-"或指定的前缀加上"."开头，则返回真。

    确定文件路径是否属于指定前缀的文档包

    如果文件属于文档包，则返回真。

    参数
    ----------
    prefix: str  
      文件名的前缀
    file_path: str
      文件路径

    返回值
    -------
    bool
      True - 文件属于指定的文档包
    """
    import os
    
    # 获取文件名
    filename = os.path.basename(file_path)
    
    # 检查文件名是否以prefix-或prefix.开头
    if filename.startswith(prefix + "-") or filename.startswith(prefix + "."):
        return True
    return False