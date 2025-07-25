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
    for cls in unique_classes:
        if not any(issubclass(cls, other) for other in unique_classes if other is not cls):
            minimal_classes.append(cls)
    
    return minimal_classes