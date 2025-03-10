def oneline(script, separator=" && "):
    """
    Converte uno script in un comando su una sola riga.  
    Questo è utile per eseguire un singolo comando SSH e passare uno script su una sola riga.

    :param script: Lo script da convertire in una singola riga.
    :param separator: Il separatore da utilizzare tra i comandi (default è " && ").
    :return: Una stringa che rappresenta lo script su una sola riga.
    """
    if isinstance(script, str):
        script = script.splitlines()
    return separator.join(line.strip() for line in script if line.strip())