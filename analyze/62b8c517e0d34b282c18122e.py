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
    
    # Obtener la traza de la excepción
    tb_list = traceback.format_exception(type(e), e, e.__traceback__)
    
    # Limitar el número de niveles de la pila de llamadas
    if len(tb_list) > max_level:
        tb_list = tb_list[:max_level]
    
    # Limitar el número de niveles de la ruta
    for i in range(len(tb_list)):
        if len(tb_list[i].splitlines()) > max_path_level:
            tb_list[i] = "\n".join(tb_list[i].splitlines()[:max_path_level]) + "\n..."
    
    # Unir la traza en una sola cadena
    formatted_trace = "".join(tb_list)
    
    return formatted_trace