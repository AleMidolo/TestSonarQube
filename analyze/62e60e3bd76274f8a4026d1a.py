def from_raw_values(cls, values):
    """
    从一组原始书签字符串值创建一个 Bookmarks 对象。

    除非您需要反序列化书签，否则不需要使用此方法。

    :param values: ASCII 字符串值（原始书签）
    :type values: Iterable[str]
    """
    bookmarks = cls()
    for value in values:
        # Assuming the Bookmarks class has a method to add a bookmark from a raw value
        bookmarks.add_bookmark_from_raw(value)
    return bookmarks