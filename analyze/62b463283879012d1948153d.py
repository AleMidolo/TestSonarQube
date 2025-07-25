def match_pubdate(node, pubdate_xpaths):
    """
    `pubdate_xpaths` सूची में पहला मेलित मान (match) लौटाता है।
    """
    for xpath in pubdate_xpaths:
        result = node.xpath(xpath)
        if result:
            return result[0]
    return None