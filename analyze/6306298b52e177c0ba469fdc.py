def xml_children_as_dict(node):
    """
    Trasforma i figli del nodo <xml> in un dizionario, con chiavi basate sul nome del tag.

    Questa è una conversione superficiale - i nodi figli non vengono elaborati ricorsivamente.
    """
    result = {}
    for child in node:
        tag = child.tag
        if tag in result:
            if isinstance(result[tag], list):
                result[tag].append(child.text)
            else:
                result[tag] = [result[tag], child.text]
        else:
            result[tag] = child.text
    return result