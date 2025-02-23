def match(filename):
    """
    Verifica se il nome file è di un tipo supportato da questo modulo

    Argomenti:
        filename: Nome file da confrontare
    Ritorna:
        False se non è una corrispondenza, True se è supportato
    """
    supported_extensions = ['.txt', '.csv', '.json', '.xml']
    return any(filename.endswith(ext) for ext in supported_extensions)