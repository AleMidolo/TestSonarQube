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
    import os
    
    # Get the full traceback
    tb_list = traceback.extract_tb(e.__traceback__)
    
    # Limit stack trace to max_level
    if len(tb_list) > max_level:
        tb_list = tb_list[-max_level:]
        
    formatted = []
    formatted.append(f"{e.__class__.__name__}: {str(e)}\n")
    
    for filename, line, func, text in tb_list:
        # Shorten path if needed
        path_parts = filename.split(os.sep)
        if len(path_parts) > max_path_level:
            filename = os.sep.join(['...'] + path_parts[-max_path_level:])
            
        formatted.append(f"  File \"{filename}\", line {line}, in {func}")
        if text:
            formatted.append(f"    {text}")
            
    return '\n'.join(formatted)