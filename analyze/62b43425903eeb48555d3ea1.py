def _create_in_regex(self) -> Pattern:
    """
    创建 in-style 参数的正则表达式。

    返回 in-style 参数的正则表达式 (:class:`re.Pattern`)。
    """
    # 匹配 in-style 参数的正则表达式模式
    # 格式为: in:value1,value2,...
    pattern = r'in:([^,\s]+(?:,[^,\s]+)*)'
    
    # 编译正则表达式并返回
    return re.compile(pattern)