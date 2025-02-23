def match_pubdate(node, pubdate_xpaths):
    """
    对于给定的节点，返回 `pubdate_xpaths` 列表中的第一个匹配项。

    返回 `pubdate_xpaths` 列表中的第一个匹配项。
    """
    for xpath in pubdate_xpaths:
        matched_nodes = node.xpath(xpath)
        if matched_nodes:
            return matched_nodes[0].text
    return None