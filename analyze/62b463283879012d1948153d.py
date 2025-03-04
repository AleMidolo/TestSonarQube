def match_pubdate(node, pubdate_xpaths):
    """
    对于给定的节点，返回 `pubdate_xpaths` 列表中的第一个匹配项。

    返回 `pubdate_xpaths` 列表中的第一个匹配项。
    """
    for xpath in pubdate_xpaths:
        try:
            # Try to find matching element using xpath
            match = node.xpath(xpath)
            if match:
                # Return first match if found
                return match[0]
        except:
            # Skip any xpath that causes errors
            continue
    
    # Return None if no matches found
    return None