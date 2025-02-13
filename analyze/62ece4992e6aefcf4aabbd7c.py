def oneline(script, separator=" && "):
    return separator.join(line for line in script.strip().splitlines() if line)