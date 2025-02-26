def strip_root(path, root):
    """
    从路径中移除根目录。如果失败，则抛出异常。

    返回值:
        一个不包含根目录的路径

    从路径中移除根目录。失败时抛出异常。
    """
    if not path.startswith(root):
        raise ValueError("路径不以根目录开头")
    
    return path[len(root):].lstrip('/')