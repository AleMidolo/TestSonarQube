def from_raw_values(cls, values):
    """
    从一组原始书签字符串值创建一个 Bookmarks 对象。

    除非您需要反序列化书签，否则不需要使用此方法。

    :param values: ASCII 字符串值（原始书签）
    :type values: Iterable[str]
    """
    # Assuming the Bookmarks class is defined elsewhere
    bookmarks = cls()
    for value in values:
        # Process each raw value and add it to the Bookmarks object
        # This is a placeholder for the actual processing logic
        bookmark = process_raw_value(value)  # Assuming process_raw_value is defined elsewhere
        bookmarks.add(bookmark)
    return bookmarks