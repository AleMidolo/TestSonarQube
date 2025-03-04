def from_raw_values(cls, values):
    """
    从一组原始书签字符串值创建一个 Bookmarks 对象。

    除非您需要反序列化书签，否则不需要使用此方法。

    :param values: ASCII 字符串值（原始书签）
    :type values: Iterable[str]
    """
    bookmarks = []
    for value in values:
        # 移除空白字符
        value = value.strip()
        
        # 跳过空行
        if not value:
            continue
            
        try:
            # 尝试解析书签字符串
            bookmark = cls._parse_raw_value(value)
            if bookmark:
                bookmarks.append(bookmark)
        except:
            # 解析失败则跳过该行
            continue
            
    # 返回新的 Bookmarks 对象
    return cls(bookmarks)