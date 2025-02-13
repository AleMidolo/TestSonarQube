def oneline(script, separator=" && "):
    """
    Converte uno script in un comando su una sola riga.  
    Questo è utile per eseguire un singolo comando SSH e passare uno script su una sola riga.

    :param script:  
    :return:
    """
    return separator.join(line.strip() for line in script.strip().splitlines() if line.strip())