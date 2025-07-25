def oneline(script, separator=" && "):
    """
    Converte uno script in un comando su una sola riga.  
    Questo è utile per eseguire un singolo comando SSH e passare uno script su una sola riga.

    :param script: String containing multiline script
    :param separator: String to use as command separator (default " && ")
    :return: Single line string with commands separated by separator
    """
    # Split script into lines and remove empty lines
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Join lines with separator
    return separator.join(lines)