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

    # Get the traceback information
    tb = traceback.extract_tb(e.__traceback__)
    tb_info = tb[:max_level]

    # Format the traceback information
    formatted_tb = []
    for frame in tb_info:
        filename, lineno, funcname, code = frame
        formatted_tb.append(f'File "{filename}", line {lineno}, in {funcname}\n    {code}')

    # Limit the number of paths shown
    if len(formatted_tb) > max_path_level:
        formatted_tb = formatted_tb[:max_path_level] + [f"... and {len(tb_info) - max_path_level} more lines"]

    # Combine everything into a single string
    result = f"{exc_type}: {exc_message}\n" + "\n".join(formatted_tb)
    return result