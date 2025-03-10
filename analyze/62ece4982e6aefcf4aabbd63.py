def is_none_string(val: any) -> bool:
    """
    检查字符串是否表示一个 None 值。
    返回值:
        如果 val 是字符串，并且 val 的小写形式是 'none'，则返回真；否则返回假。
    """
    return isinstance(val, str) and val.lower() == 'none'