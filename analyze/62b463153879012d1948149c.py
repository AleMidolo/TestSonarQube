def select_filenames_by_prefix(prefix, files):
    """
    对于文件列表中的每个文件，返回所有与给定前缀匹配的文件。

    获取属于文档包的文件。

    返回 `files` 列表中文件名以 `prefix` 开头的文件。

    参数
    ----------
    prefix: str  
        文件名前缀  
    files: list[str]  
        文件路径列表  

    返回值
    -------
    list
        文件路径列表，其中的文件名与前缀 `prefix` 匹配。
    """
    # 创建一个空列表来存储匹配的文件
    matched_files = []
    
    # 遍历文件列表
    for file in files:
        # 获取文件名(不包含路径)
        filename = file.split('/')[-1]
        
        # 检查文件名是否以prefix开头
        if filename.startswith(prefix):
            matched_files.append(file)
            
    return matched_files