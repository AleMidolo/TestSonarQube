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
    
    # Ottieni lo stack trace
    stack_trace = traceback.format_exc()
    
    # Limita il numero di livelli dello stack
    stack_lines = stack_trace.splitlines()
    if len(stack_lines) > max_level * 2:  # Ogni livello ha 2 righe
        stack_lines = stack_lines[:max_level * 2]
        stack_lines.append("... (stack trace troncato)")
    
    # Limita il numero di livelli del percorso
    formatted_trace = "\n".join(stack_lines)
    if max_path_level > 0:
        formatted_trace = "\n".join(stack_lines[:max_path_level * 2])
        formatted_trace += "\n... (percorso troncato)"
    
    # Aggiungi il messaggio dell'eccezione
    exception_message = str(e)
    formatted_trace = f"{exception_message}\n{formatted_trace}"
    
    return formatted_trace