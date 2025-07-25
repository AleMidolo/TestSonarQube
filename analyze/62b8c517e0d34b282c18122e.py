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
    if len(stack_lines) > max_level:
        stack_lines = stack_lines[:max_level]
        stack_lines.append("... (stack trace troncato)")
    
    # Limita il numero di livelli del percorso
    formatted_trace = "\n".join(stack_lines)
    if len(formatted_trace.splitlines()) > max_path_level:
        formatted_trace = "\n".join(formatted_trace.splitlines()[:max_path_level])
        formatted_trace += "\n... (percorso troncato)"
    
    return formatted_trace