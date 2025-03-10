def from_raw_values(cls, values):
    """
    从一组原始书签字符串值创建一个 Bookmarks 对象。

    除非您需要反序列化书签，否则不需要使用此方法。

    :param values: ASCII 字符串值（原始书签）
    :type values: Iterable[str]
    """
    # Assuming Bookmarks is a class that can be initialized with the processed values
    processed_values = [value.strip() for value in values]  # Example processing step
    return cls(processed_values)