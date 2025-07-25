def strip_root(percorso, radice):
    """
    Rimuovi la radice dal percorso, genera un'eccezione in caso di errore.
    """
    if not percorso.startswith(radice):
        raise ValueError("Il percorso non inizia con la radice specificata.")
    return percorso[len(radice):]