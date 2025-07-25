import os

def make_find_paths(find_paths):
    """
    给定一个路径序列，将所有路径转换为 glob 模式。现有的模式保持不变。

    参数:
      find_paths: 路径序列
    返回:
      转换后的路径元组

    给定通过 `--find` 参数传递的一系列路径片段或模式，将所有路径片段转换为 glob 模式。现有的模式保持不变。

    例如，给定 `find_paths` 为：

    `['foo.txt', 'pp:root/somedir']`

    将其转换为：

    `['sh:**/*foo.txt*/**', 'pp:root/somedir']`
    """
    result = []
    for path in find_paths:
        if path.startswith(('sh:', 'pp:')):
            result.append(path)
        else:
            # Convert path to glob pattern
            glob_pattern = f"sh:**/*{os.path.basename(path)}*/**"
            result.append(glob_pattern)
    return tuple(result)