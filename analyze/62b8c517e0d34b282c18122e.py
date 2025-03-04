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
    tb = traceback.extract_tb(e.__traceback__)
    
    # Format the exception message
    error_msg = f"{type(e).__name__}: {str(e)}\n"
    
    # Add stack trace info
    for i, frame in enumerate(tb[:max_level]):
        filename = frame.filename
        
        # Shorten path if needed
        if max_path_level > 0:
            path_parts = filename.split(os.sep)
            if len(path_parts) > max_path_level:
                filename = os.sep.join(['...'] + path_parts[-max_path_level:])
                
        # Add frame info
        error_msg += f"  File \"{filename}\", line {frame.lineno}, in {frame.name}\n"
        if frame.line:
            error_msg += f"    {frame.line}\n"
            
        if i >= max_level - 1:
            error_msg += "    ...\n"
            break
            
    return error_msg