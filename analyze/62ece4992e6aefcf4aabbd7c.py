def oneline(script, separator=" && "):
    """
    Converte uno script in un comando su una sola riga.  
    Questo è utile per eseguire un singolo comando SSH e passare uno script su una sola riga.

    :param script: Lo script da convertire in una singola riga.
    :param separator: Il separatore da utilizzare tra i comandi (default è " && ").
    :return: Una stringa che rappresenta lo script su una sola riga.
    """
    lines = script.strip().splitlines()
    return separator.join(line.strip() for line in lines if line.strip())