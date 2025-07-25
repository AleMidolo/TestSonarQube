def parse_version(s: str) -> tuple[int, ...]:
    """
    将由点连接的字符串转换为由整数组成的元组。
    """
    # 按点分割字符串,将每个部分转换为整数,最后转换为元组返回
    return tuple(int(x) for x in s.split('.'))