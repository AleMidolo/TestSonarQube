def match_pubdate(node, pubdate_xpaths):
    """
    Restituisce la prima corrispondenza nella lista `pubdate_xpaths`.
    """
    for xpath in pubdate_xpaths:
        result = node.xpath(xpath)
        if result:
            return result[0]
    return None