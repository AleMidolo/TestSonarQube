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
    
    # Ottieni la traccia dello stack
    stack_trace = traceback.format_exc(limit=max_level)
    
    # Limita il percorso del file se necessario
    if max_path_level > 0:
        lines = stack_trace.splitlines()
        for i in range(len(lines)):
            if "File" in lines[i]:
                path_parts = lines[i].split(",")[0].split("File ")[1].strip().split("/")
                if len(path_parts) > max_path_level:
                    lines[i] = lines[i].replace("/".join(path_parts), "/".join(path_parts[-max_path_level:]))
        stack_trace = "\n".join(lines)
    
    # Aggiungi il messaggio dell'eccezione
    exception_message = f"Exception: {str(e)}\n"
    full_message = exception_message + stack_trace
    
    return full_message