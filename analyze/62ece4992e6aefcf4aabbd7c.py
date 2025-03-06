def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: Lista de comandos o un string con comandos separados por saltos de línea.
    :param separator: Separador entre comandos (por defecto " && ").
    :return: String con los comandos concatenados en una sola línea.
    """
    if isinstance(script, str):
        script = script.splitlines()
    return separator.join(command.strip() for command in script if command.strip())