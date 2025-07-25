def strip_root(path, root):
    """
    从路径中移除根目录。如果失败，则抛出异常。

    返回值:
      一个不包含根目录的路径

    从路径中移除根目录。失败时抛出异常。
    """
    # 标准化路径格式
    path = path.replace('\\', '/')
    root = root.replace('\\', '/')
    
    # 确保root以/结尾
    if not root.endswith('/'):
        root += '/'
        
    # 检查path是否以root开头
    if not path.startswith(root):
        raise ValueError(f"Path '{path}' does not start with root '{root}'")
        
    # 移除root
    stripped_path = path[len(root):]
    
    # 移除开头的/
    if stripped_path.startswith('/'):
        stripped_path = stripped_path[1:]
        
    return stripped_path