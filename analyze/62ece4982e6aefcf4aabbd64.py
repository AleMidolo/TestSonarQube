def strip_root(path, root):
    """
    从路径中移除根目录。如果失败，则抛出异常。

    返回值:
        一个不包含根目录的路径

    从路径中移除根目录。失败时抛出异常。
    """
    if not path.startswith(root):
        raise ValueError(f"Path '{path}' does not start with root '{root}'")
    stripped_path = path[len(root):]
    if stripped_path.startswith('/'):
        stripped_path = stripped_path[1:]
    return stripped_path