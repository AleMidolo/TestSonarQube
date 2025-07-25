import re

def unquote(name):
    """
    使用正则表达式从给定的名称中移除引号。

    参数:
        name: 输入的名称
    返回值:
        移除引号后的名称
    从给定的名称中移除引号。
    """
    return re.sub(r'^[\'"]|[\'"]$', '', name)