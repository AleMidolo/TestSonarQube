def match_pubdate(node, pubdate_xpaths):
    """
    Restituisce la prima corrispondenza nella lista `pubdate_xpaths`.
    
    :param node: Il nodo XML/HTML da cui cercare.
    :param pubdate_xpaths: Lista di percorsi XPath da provare.
    :return: Il primo valore trovato corrispondente a uno degli XPath, o None se nessuno corrisponde.
    """
    for xpath in pubdate_xpaths:
        result = node.xpath(xpath)
        if result:
            return result[0]
    return None