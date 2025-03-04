def minimalBases(classes):
    """
    Riduce una lista di classi base al suo equivalente minimo ordinato.
    """
    if not classes:
        return []
        
    # Rimuove le classi duplicate mantenendo l'ordine
    unique_classes = []
    for cls in classes:
        if cls not in unique_classes:
            unique_classes.append(cls)
            
    # Rimuove le classi che sono già base di altre classi nella lista
    minimal = []
    for i, cls in enumerate(unique_classes):
        is_redundant = False
        for other in unique_classes[i+1:]:
            if issubclass(other, cls):
                is_redundant = True
                break
        if not is_redundant:
            minimal.append(cls)
            
    return minimal