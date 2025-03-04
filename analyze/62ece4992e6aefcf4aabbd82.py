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
    import re
    
    # 如果已经是正则表达式模式对象,直接返回
    if isinstance(pattern, re.Pattern):
        return pattern
        
    # 如果是字符串类型
    if isinstance(pattern, str):
        # 根据strip参数决定是否去除空格
        if strip:
            pattern = pattern.strip()
        # 编译为正则表达式模式对象并返回    
        return re.compile(pattern)
        
    # 其他类型抛出异常
    raise TypeError(f"pattern must be string or Pattern object, not {type(pattern)}")