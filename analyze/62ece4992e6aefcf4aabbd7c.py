def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: String containing multiline script
    :param separator: String to use as command separator (default " && ")
    :return: Single line string with commands joined by separator
    """
    # Split script into lines and remove empty lines
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Join all non-empty lines with the separator
    return separator.join(lines)