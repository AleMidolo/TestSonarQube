import os

def files_list(path):
    """
    返回给定路径中的文件。
    返回 `path` 中的文件。
    """
    if not os.path.exists(path):
        return []
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]