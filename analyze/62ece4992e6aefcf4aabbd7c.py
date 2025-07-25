def oneline(script, separator=" && "):
    # Remove empty lines and leading/trailing whitespace
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Join all non-empty lines with the separator
    return separator.join(lines)