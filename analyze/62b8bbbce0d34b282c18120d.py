import os

def is_file_exist(file_name):
    """
    Controlla se il nome del file esiste.
    :param file_name: Nome del file.
    :type file_name: str
    :return: Restituisce True (esiste), False (non esiste o nome del file non valido).
    :rtype: bool
    """
    if not isinstance(file_name, str) or not file_name:
        return False
    return os.path.isfile(file_name)