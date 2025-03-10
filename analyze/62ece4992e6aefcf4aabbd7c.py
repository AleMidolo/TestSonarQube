def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: El script a convertir en una sola línea.
    :param separator: El separador entre comandos (por defecto es " && ").
    :return: El script convertido en una sola línea.
    """
    if isinstance(script, str):
        return script
    elif isinstance(script, list):
        return separator.join(script)
    else:
        raise TypeError("El script debe ser una cadena o una lista de cadenas.")