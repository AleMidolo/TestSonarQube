def oneline(script, separator=" && "):
    """
    Converte uno script in un comando su una sola riga.  
    Questo è utile per eseguire un singolo comando SSH e passare uno script su una sola riga.

    :param script: Lo script da convertire in una singola riga.
    :param separator: Il separatore da utilizzare tra i comandi (default è " && ").
    :return: Una stringa che rappresenta lo script su una sola riga.
    """
    if isinstance(script, str):
        lines = script.splitlines()
    elif isinstance(script, list):
        lines = script
    else:
        raise TypeError("Il parametro 'script' deve essere una stringa o una lista di stringhe.")
    
    # Rimuove le righe vuote e gli spazi bianchi in eccesso
    lines = [line.strip() for line in lines if line.strip()]
    
    # Unisce le righe con il separatore specificato
    return separator.join(lines)