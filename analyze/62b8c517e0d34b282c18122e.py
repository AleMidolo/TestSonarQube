def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Formatta un'eccezione.
    :param e: Qualsiasi istanza di eccezione.
    :type e: Exception
    :param max_level: Livello massimo dello stack delle chiamate (predefinito 30)
    :type max_level: int
    :param max_path_level: Livello massimo del percorso (predefinito 5)
    :type max_path_level: int
    :return: La stringa leggibile dell'eccezione
    :rtype: str
    """
    import traceback
    import sys

    # Ottieni il traceback
    tb = sys.exc_info()[2]
    if tb is None:
        tb = e.__traceback__

    # Limita il numero di livelli dello stack
    stack = traceback.extract_tb(tb, limit=max_level)

    # Costruisci il percorso dell'eccezione
    path = []
    for frame in stack:
        file_path = frame.filename
        # Limita il livello del percorso
        if len(path) < max_path_level:
            path.append(file_path)
        else:
            break

    # Costruisci la stringa dell'eccezione
    exception_str = f"Exception: {str(e)}\n"
    exception_str += f"Type: {type(e).__name__}\n"
    exception_str += f"Traceback (most recent call last):\n"
    for frame in stack:
        exception_str += f"  File \"{frame.filename}\", line {frame.lineno}, in {frame.name}\n"
        exception_str += f"    {frame.line}\n"
    exception_str += f"Path: {' -> '.join(path)}\n"

    return exception_str