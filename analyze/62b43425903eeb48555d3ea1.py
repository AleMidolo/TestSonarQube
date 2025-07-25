def _create_in_regex(self) -> Pattern:
    """
    创建 in-style 参数的正则表达式。

    返回 in-style 参数的正则表达式 (:class:`re.Pattern`)。
    """
    # 构建正则表达式模式
    # 匹配格式: {param_name in [val1,val2,...]}
    pattern = r"""
    \{              # 开始大括号
    ([^{}:\s]+)     # 参数名 (不包含大括号、冒号和空白字符)
    \s+in\s+        # in 关键字
    \[              # 开始方括号
    ([^\]]+)        # 值列表 (除了右方括号外的任何字符)
    \]              # 结束方括号
    \}              # 结束大括号
    """
    
    # 编译正则表达式并返回
    return re.compile(pattern, re.VERBOSE)