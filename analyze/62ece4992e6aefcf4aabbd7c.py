def oneline(script, separator=" && "):
    # Remove empty lines and leading/trailing whitespace
    lines = [line.strip() for line in script.splitlines() if line.strip()]
    
    # Join all non-empty lines with the separator
    return separator.join(lines)