def strip_root(percorso, radice):
    """
    Rimuovi la radice dal percorso, genera un'eccezione in caso di errore.
    
    :param percorso: Il percorso completo da cui rimuovere la radice.
    :param radice: La radice da rimuovere dal percorso.
    :return: Il percorso senza la radice.
    :raises ValueError: Se la radice non è un prefisso del percorso.
    """
    if not percorso.startswith(radice):
        raise ValueError("La radice non è un prefisso del percorso.")
    
    return percorso[len(radice):]