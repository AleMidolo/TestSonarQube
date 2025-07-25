def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script:  
    :return:
    """
    return separator.join(line.strip() for line in script.strip().splitlines() if line.strip())