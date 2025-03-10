def minimalBases(classes):
    """
    Reduce una lista de clases base a su equivalente mínimo ordenado.
    """
    # Eliminar duplicados
    unique_classes = list(dict.fromkeys(classes))
    
    # Ordenar las clases
    unique_classes.sort(key=lambda x: x.__name__)
    
    # Eliminar clases que son subclases de otras en la lista
    minimal_classes = []
    for i, cls in enumerate(unique_classes):
        is_minimal = True
        for other_cls in unique_classes[i+1:]:
            if issubclass(cls, other_cls):
                is_minimal = False
                break
        if is_minimal:
            minimal_classes.append(cls)
    
    return minimal_classes