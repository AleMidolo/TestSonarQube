def oneline(script, separator=" && "):
    """
    Converte uno script in un comando su una sola riga.  
    Questo è utile per eseguire un singolo comando SSH e passare uno script su una sola riga.

    :param script: Lo script da convertire in una singola riga.
    :param separator: Il separatore da utilizzare tra i comandi (default è " && ").
    :return: Una stringa che rappresenta lo script su una sola riga.
    """
    if isinstance(script, str):
        # Se lo script è una stringa singola, dividila in righe e uniscile
        lines = script.strip().splitlines()
        return separator.join(line.strip() for line in lines if line.strip())
    elif isinstance(script, list):
        # Se lo script è una lista di comandi, uniscili direttamente
        return separator.join(cmd.strip() for cmd in script if cmd.strip())
    else:
        raise ValueError("Il parametro 'script' deve essere una stringa o una lista di stringhe.")