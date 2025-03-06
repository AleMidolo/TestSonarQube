def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: Lista de comandos o un string con saltos de linea.
    :param separator: Separador entre comandos (por defecto " && ").
    :return: String con el script convertido en una sola linea.
    """
    if isinstance(script, str):
        lines = script.strip().split('\n')
    elif isinstance(script, list):
        lines = script
    else:
        raise ValueError("El script debe ser una lista de comandos o un string con saltos de linea.")
    
    return separator.join(line.strip() for line in lines if line.strip())