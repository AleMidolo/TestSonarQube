def match_pubdate(node, pubdate_xpaths):
    """
    Returns the first match in the pubdate_xpaths list
    """
    for xpath in pubdate_xpaths:
        matches = node.xpath(xpath)
        if matches:
            return matches[0]
    return None