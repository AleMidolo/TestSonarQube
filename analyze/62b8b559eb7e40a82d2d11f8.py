def minimalBases(classes):
    """
    Reduce una lista de clases base a su equivalente mínimo ordenado.
    """
    # Si no hay clases, retornar lista vacía
    if not classes:
        return []
        
    # Eliminar duplicados manteniendo el orden
    unique_classes = []
    for cls in classes:
        if cls not in unique_classes:
            unique_classes.append(cls)
            
    # Eliminar clases que son ancestros de otras clases en la lista
    minimal = []
    for i, cls in enumerate(unique_classes):
        is_ancestor = False
        for other in unique_classes[i+1:]:
            if issubclass(other, cls):
                is_ancestor = True
                break
        if not is_ancestor:
            minimal.append(cls)
            
    return minimal