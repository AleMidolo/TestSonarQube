def strip_root(percorso, radice):
    """
    Rimuovi la radice dal percorso, genera un'eccezione in caso di errore.
    """
    if not isinstance(percorso, str) or not isinstance(radice, str):
        raise ValueError("Entrambi i parametri devono essere stringhe.")
    
    if not percorso.startswith(radice):
        raise ValueError("Il percorso non inizia con la radice fornita.")
    
    return percorso[len(radice):]