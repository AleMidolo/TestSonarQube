def xml_children_as_dict(node):
    """
    Trasforma i figli del nodo <xml> in un dizionario, con chiavi basate sul nome del tag.

    Questa è una conversione superficiale - i nodi figli non vengono elaborati ricorsivamente.
    """
    return {child.tag: child for child in node}