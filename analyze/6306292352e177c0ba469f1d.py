def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    在文本中查找标签。

    尽量忽略代码块中的标签。

    可选地，如果传入了一个 "replacer"，则会使用调用该 replacer 函数（参数为标签单词）的返回值来替换该标签单词。

    返回一个包含标签的集合以及原始文本或替换后的文本。
    """
    # 初始化标签集合和结果文本
    tags = set()
    result_text = text
    
    # 标记是否在代码块内
    in_code_block = False
    lines = text.split('\n')
    
    # 遍历每一行
    for i, line in enumerate(lines):
        # 检查是否进入或离开代码块
        if line.strip().startswith('