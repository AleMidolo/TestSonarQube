def minimalBases(classes):
    """
    Reduce una lista de clases base a su equivalente mínimo ordenado.
    """
    # Eliminar duplicados
    unique_classes = list(dict.fromkeys(classes))
    
    # Ordenar las clases
    unique_classes.sort(key=lambda x: x.__name__)
    
    # Eliminar clases que ya están en la jerarquía de otras
    minimal = []
    for cls in unique_classes:
        if not any(issubclass(other, cls) for other in unique_classes if other != cls):
            minimal.append(cls)
    
    return minimal