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
    
    # 如果已经是编译好的正则表达式模式,直接返回
    if isinstance(pattern, re.Pattern):
        return pattern
        
    # 如果是字符串,先转换为字符串类型
    if not isinstance(pattern, str):
        pattern = str(pattern)
        
    # 根据strip参数决定是否去除首尾空格
    if strip:
        pattern = pattern.strip()
        
    # 编译正则表达式并返回
    try:
        return re.compile(pattern)
    except re.error as e:
        raise ValueError(f"Invalid regular expression pattern: {str(e)}")