def _create_in_regex(self) -> Pattern:
    """
    创建 in-style 参数的正则表达式。

    返回 in-style 参数的正则表达式 (:class:`re.Pattern`)。
    """
    # 构建正则表达式模式
    # 匹配格式: {param_name in [val1,val2,...]}
    pattern = r"""
    \{              # 开始大括号
    ([^{}:\s]+)     # 参数名 - 捕获组1
    \s+in\s+        # in关键字
    \[              # 开始方括号
    ([^\]]+)        # 值列表 - 捕获组2
    \]              # 结束方括号
    \}              # 结束大括号
    """
    
    # 编译正则表达式,使用verbose模式以支持注释和空白
    return re.compile(pattern, re.VERBOSE)