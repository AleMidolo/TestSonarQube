def oneline(script, separator=" && "):
    """
    Converte uno script in un comando su una sola riga.  
    Questo è utile per eseguire un singolo comando SSH e passare uno script su una sola riga.

    :param script: String containing multiline script
    :param separator: String to use as command separator (default: " && ")
    :return: String with commands joined on a single line
    """
    # Split script into lines and remove empty lines
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Join non-empty lines with the separator
    return separator.join(lines)