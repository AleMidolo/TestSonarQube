def xml_children_as_dict(node):
    """
    Convierte los hijos del nodo <xml> en un diccionario, donde las claves son los nombres de las etiquetas.

    Esta es solo una conversión superficial: los nodos hijos no se procesan de manera recursiva.
    """
    result = {}
    for child in node:
        # Obtiene el nombre de la etiqueta sin el namespace
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        result[tag] = child
    return result