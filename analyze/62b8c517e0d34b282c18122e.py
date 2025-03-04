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

    # Get the exception type and message
    exc_type = type(e).__name__
    exc_message = str(e)

    # Get the traceback
    tb = traceback.extract_tb(e.__traceback__)
    tb = tb[:max_level]  # Limit the traceback to max_level

    # Format the traceback
    formatted_tb = []
    for frame in tb:
        filename, lineno, funcname, code = frame
        formatted_tb.append(f'File "{filename}", line {lineno}, in {funcname}\n    {code}')

    # Limit the number of paths in the traceback
    if len(formatted_tb) > max_path_level:
        formatted_tb = formatted_tb[:max_path_level] + [f"... and {len(tb) - max_path_level} more lines"]

    # Combine everything into a final string
    result = f"{exc_type}: {exc_message}\n" + "\n".join(formatted_tb)
    return result