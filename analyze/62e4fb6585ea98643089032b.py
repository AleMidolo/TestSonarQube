def parse_version(s: str) -> tuple[int, ...]:
    """
    将由点连接的字符串转换为由整数组成的元组。
    """
    return tuple(map(int, s.split('.')))