def replace_dots(value, arg):
    """
    将给定字符串中的所有 . 替换为 arg 提供的值。
    参数:  
      value: 原始字符串  
      arg: 用于替换 '.' 的新字符串  
    返回值:  
      str: 替换后的字符串
    """
    return value.replace('.', arg)