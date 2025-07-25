def minimalBases(classes):
    """
    Riduce una lista di classi base al suo equivalente minimo ordinato.
    """
    # Creiamo un set per rimuovere duplicati
    unique_classes = set(classes)
    
    # Rimuoviamo le classi che sono superclassi di altre classi nel set
    minimal_classes = []
    for cls in unique_classes:
        if not any(issubclass(other_cls, cls) for other_cls in unique_classes if other_cls != cls):
            minimal_classes.append(cls)
    
    # Ordiniamo le classi rimanenti
    minimal_classes.sort(key=lambda x: x.__name__)
    
    return minimal_classes