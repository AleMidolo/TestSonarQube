def oneline(script, seperator=" && "):
    """
    converts a script to one line command.
    THis is useful to run a single ssh command and pass a one line script.

    :param script: String containing multiline script
    :return: String with commands joined by separator
    """
    # Split script into lines and remove empty lines
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Join lines with separator
    return seperator.join(lines)