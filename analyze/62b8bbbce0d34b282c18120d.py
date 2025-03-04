def is_file_exist(file_name):
    """
    Controlla se il nome del file esiste.
    :param file_name: Nome del file.
    :type file_name: str 
    :return: Restituisce True (esiste), False (non esiste o nome del file non valido).
    :rtype: bool
    """
    import os
    
    try:
        return os.path.exists(file_name)
    except:
        return False