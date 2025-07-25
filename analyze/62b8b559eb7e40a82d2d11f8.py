def minimalBases(classes):
    """
    Riduce una lista di classi base al suo equivalente minimo ordinato.
    """
    # Creiamo un insieme per memorizzare le classi uniche
    unique_classes = set()
    
    # Iteriamo attraverso le classi
    for cls in classes:
        # Se la classe non è già nell'insieme, la aggiungiamo
        if cls not in unique_classes:
            unique_classes.add(cls)
    
    # Convertiamo l'insieme in una lista ordinata
    return sorted(unique_classes, key=lambda x: x.__name__)