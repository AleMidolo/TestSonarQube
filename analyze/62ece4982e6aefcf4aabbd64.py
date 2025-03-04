def strip_root(percorso, radice):
    """
    Rimuovi la radice dal percorso, genera un'eccezione in caso di errore.
    """
    if not percorso.startswith(radice):
        raise ValueError(f"Il percorso '{percorso}' non inizia con la radice '{radice}'")
    
    # Rimuovi la radice dal percorso
    stripped = percorso[len(radice):]
    
    # Rimuovi eventuali separatori iniziali
    while stripped.startswith('/') or stripped.startswith('\\'):
        stripped = stripped[1:]
        
    return stripped