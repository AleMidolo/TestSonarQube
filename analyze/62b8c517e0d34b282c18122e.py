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
    tb = traceback.format_exception(type(e), e, e.__traceback__)
    
    # Limitar el número de niveles de la pila de llamadas
    if len(tb) > max_level:
        tb = tb[:max_level]
        tb.append(f"... (truncated to {max_level} levels)")
    
    # Limitar el número de niveles de la ruta
    for i in range(len(tb)):
        parts = tb[i].split('\n')
        if len(parts) > max_path_level:
            parts = parts[:max_path_level]
            parts.append(f"... (truncated to {max_path_level} levels)")
        tb[i] = '\n'.join(parts)
    
    # Unir la traza en una sola cadena
    return ''.join(tb)