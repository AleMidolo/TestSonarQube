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
    return [file for file in files if file.startswith(prefix)]