def match_pubdate(node, pubdate_xpaths):
    """
    对于给定的节点，返回 `pubdate_xpaths` 列表中的第一个匹配项。

    返回 `pubdate_xpaths` 列表中的第一个匹配项。
    """
    for xpath in pubdate_xpaths:
        result = node.xpath(xpath)
        if result:
            return result[0]
    return None