def oneline(script, separator=" && "):
    # Split script into lines and remove empty lines
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Join lines with separator
    return separator.join(lines)