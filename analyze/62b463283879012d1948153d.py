def match_pubdate(node, pubdate_xpaths):
    """
    Restituisce la prima corrispondenza nella lista `pubdate_xpaths`.

    :param node: L'elemento XML/HTML da cui cercare.
    :param pubdate_xpaths: Lista di percorsi XPath da provare.
    :return: Il primo valore trovato o None se nessun percorso corrisponde.
    """
    for xpath in pubdate_xpaths:
        result = node.xpath(xpath)
        if result:
            return result[0]
    return None