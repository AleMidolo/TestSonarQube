def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: Lista de comandos o cadena con saltos de línea.
    :param separator: Separador entre comandos (por defecto " && ").
    :return: Cadena con los comandos unidos en una sola línea.
    """
    if isinstance(script, list):
        return separator.join(script)
    elif isinstance(script, str):
        return separator.join(script.strip().splitlines())
    else:
        raise TypeError("El parámetro 'script' debe ser una lista o una cadena.")