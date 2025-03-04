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
    exception_type = type(e).__name__
    exception_message = str(e)

    # Get the traceback information
    tb = traceback.extract_tb(e.__traceback__)
    tb_info = []

    for frame in tb[:max_level]:
        filename, lineno, funcname, code = frame
        tb_info.append(f'File "{filename}", line {lineno}, in {funcname}\n  {code}')

    # Limit the number of paths shown
    if len(tb_info) > max_path_level:
        tb_info = tb_info[:max_path_level] + [f"... and {len(tb) - max_path_level} more lines"]

    # Combine all parts into a single string
    formatted_exception = f"{exception_type}: {exception_message}\n" + "\n".join(tb_info)
    
    return formatted_exception