import re

def get_pattern(pattern, strip=True):
    """
    将字符串转换为正则表达式模式对象

    参数:
      pattern: 字符串或正则表达式模式对象
      strip: 布尔值，是否去除字符串开头和结尾的空格
    返回值:
      正则表达式模式对象

    此方法将给定的字符串转换为正则表达式模式。
    """
    if isinstance(pattern, str):
        if strip:
            pattern = pattern.strip()
        return re.compile(pattern)
    elif isinstance(pattern, re.Pattern):
        return pattern
    else:
        raise TypeError("pattern must be a string or a compiled regex pattern")