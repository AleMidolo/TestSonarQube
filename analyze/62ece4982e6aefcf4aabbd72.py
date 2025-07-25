def unquote(name):
    """
    Rimuovi le virgolette dal nome fornito.
    """
    if name.startswith('"') and name.endswith('"'):
        return name[1:-1]
    elif name.startswith("'") and name.endswith("'"):
        return name[1:-1]
    return name