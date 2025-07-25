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
    tb_list = traceback.extract_tb(e.__traceback__)
    tb_list = tb_list[:max_level]

    # Formatear la traza
    formatted_trace = []
    for frame in tb_list:
        filename, lineno, name, line = frame
        if tb_list.index(frame) < max_path_level:
            formatted_trace.append(f'File "{filename}", line {lineno}, in {name}\n    {line}')
    
    # Obtener el mensaje de la excepción
    exception_message = str(e)

    # Unir todo en una cadena
    result = f"{exception_message}\nTraceback (most recent call last):\n" + "\n".join(formatted_trace)
    return result