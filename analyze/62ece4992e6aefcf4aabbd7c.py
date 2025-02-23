def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: El script que se desea convertir en una sola línea.
    :return: El script convertido en una sola línea.
    """
    return separator.join(line.strip() for line in script.strip().splitlines() if line.strip())