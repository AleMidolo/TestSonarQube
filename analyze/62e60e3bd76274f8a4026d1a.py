def from_raw_values(cls, values):
    """
    从一组原始书签字符串值创建一个 Bookmarks 对象。

    除非您需要反序列化书签，否则不需要使用此方法。

    :param values: ASCII 字符串值（原始书签）
    :type values: Iterable[str]
    """
    bookmarks = []
    for value in values:
        # Assuming the raw value is a string that can be directly used
        # as a bookmark. Modify this logic as needed.
        bookmarks.append(value)
    return cls(bookmarks)