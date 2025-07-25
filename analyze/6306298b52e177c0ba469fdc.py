def xml_children_as_dict(node):
    """
    Convierte los hijos del nodo <xml> en un diccionario, donde las claves son los nombres de las etiquetas.

    Esta es solo una conversión superficial: los nodos hijos no se procesan de manera recursiva.
    """
    return {child.tag: child for child in node}