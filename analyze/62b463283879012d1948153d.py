def match_pubdate(node, pubdate_xpaths):
    """
    Devuelve la primera coincidencia en la lista de 'pubdate_xpaths'.
    """
    for xpath in pubdate_xpaths:
        match = node.xpath(xpath)
        if match:
            return match[0]
    return None