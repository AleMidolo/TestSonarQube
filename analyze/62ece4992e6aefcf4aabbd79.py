import re

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
    converted_paths = []
    for path in find_paths:
        if re.match(r'^[a-zA-Z]+:', path):
            # 如果路径已经是模式（如 'pp:root/somedir'），则保持不变
            converted_paths.append(path)
        else:
            # 否则将路径转换为 glob 模式
            converted_paths.append(f'sh:**/*{path}*/**')
    return tuple(converted_paths)