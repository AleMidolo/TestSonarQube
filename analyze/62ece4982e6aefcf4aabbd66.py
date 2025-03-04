def was_processed(processed, path_name, verbose):
    """
    Verifica se un file o una directory è già stato elaborato.

    Per prevenire la ricorsione, espandi il nome del percorso a un percorso assoluto
    e chiama questa funzione con un set che memorizzerà tutte le voci e la voce da testare.
    Se la voce è già presente nel set, segnala il problema e restituisci ``True``.
    Altrimenti, aggiungi la voce al set e restituisci ``False`` per consentire l'elaborazione del percorso.

    Args:
        processed: Set per memorizzare i percorsi già elaborati
        path_name: Percorso di una directory o di un file
        verbose: True se è richiesta un'uscita dettagliata

    Returns:
        True se il percorso è già presente nel set. False altrimenti.
    """
    import os

    absolute_path = os.path.abspath(path_name)

    if absolute_path in processed:
        if verbose:
            print(f"Il percorso '{absolute_path}' è già stato elaborato.")
        return True
    else:
        processed.add(absolute_path)
        return False