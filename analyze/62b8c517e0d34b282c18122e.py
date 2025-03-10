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
    
    # Estrai lo stack trace
    stack_trace = traceback.format_exc()
    
    # Limita il numero di livelli dello stack
    stack_lines = stack_trace.splitlines()
    if len(stack_lines) > max_level:
        stack_lines = stack_lines[:max_level]
        stack_lines.append("... (stack trace truncated)")
    
    # Limita il numero di livelli del percorso
    path_lines = []
    for line in stack_lines:
        if "File" in line and "line" in line:
            parts = line.split(", ")
            if len(parts) > max_path_level:
                parts = parts[:max_path_level]
                parts.append("... (path truncated)")
            line = ", ".join(parts)
        path_lines.append(line)
    
    # Unisci le linee in una stringa
    formatted_trace = "\n".join(path_lines)
    
    # Aggiungi il messaggio dell'eccezione
    exception_message = str(e)
    formatted_exception = f"{exception_message}\n{formatted_trace}"
    
    return formatted_exception