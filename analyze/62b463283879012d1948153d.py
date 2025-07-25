def match_pubdate(node, pubdate_xpaths):
    """
    Devuelve la primera coincidencia en la lista de 'pubdate_xpaths'.
    """
    for xpath in pubdate_xpaths:
        try:
            match = node.xpath(xpath)
            if match:
                return match[0]
        except:
            continue
    return None