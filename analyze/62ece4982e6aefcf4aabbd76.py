def match(filename):
    """
    Verifica se il nome file è di un tipo supportato da questo modulo

    Argomenti:
        filename: Nome file da confrontare
    Ritorna:
        False se non è una corrispondenza, True se è supportato
    """
    # Lista delle estensioni supportate
    supported_extensions = ['.txt', '.doc', '.docx', '.pdf', '.rtf']
    
    # Converte il filename in minuscolo per un confronto case-insensitive
    filename = filename.lower()
    
    # Verifica se il file termina con una delle estensioni supportate
    for ext in supported_extensions:
        if filename.endswith(ext):
            return True
            
    return False