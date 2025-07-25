def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Formatear una excepción.  
    :param e: Cualquier instancia de excepción.  
    :type e: Exception  
    :param max_level: Nivel máximo de la pila de llamadas (por defecto 30).  
    :type max_level: int  
    :param max_path_level: Nivel máximo de la ruta (por defecto 5).  
    :type max_path_level: int  
    :return: La cadena legible de la excepción.  
    :rtype: str  
    """
    import traceback

    # Limitar la profundidad de la pila de llamadas
    tb_lines = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
    tb_lines = tb_lines[:max_level]

    # Formatear la ruta de la excepción
    formatted_tb = ''.join(tb_lines)
    exception_message = f"Exception: {str(e)}\nTraceback (most recent call last):\n{formatted_tb}"

    # Limitar la profundidad de la ruta
    if max_path_level > 0:
        lines = exception_message.splitlines()
        limited_lines = lines[:max_path_level + 2]  # +2 for the exception message and traceback header
        exception_message = '\n'.join(limited_lines)

    return exception_message