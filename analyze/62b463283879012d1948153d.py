def match_pubdate(node, pubdate_xpaths):
    """
    Returns the first match in the pubdate_xpaths list
    """
    for xpath in pubdate_xpaths:
        result = node.xpath(xpath)
        if result:
            return result[0]
    return None