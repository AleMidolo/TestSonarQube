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
    import os
    
    # Obtener el traceback como lista de strings
    tb_list = traceback.format_exception(type(e), e, e.__traceback__, limit=max_level)
    
    # Procesar cada línea del traceback
    processed_lines = []
    for line in tb_list:
        # Acortar rutas largas
        if 'File "' in line:
            parts = line.split('File "')
            path = parts[1].split('"')[0]
            path_parts = path.split(os.sep)
            if len(path_parts) > max_path_level:
                shortened_path = os.sep.join(['...'] + path_parts[-max_path_level:])
                line = parts[0] + 'File "' + shortened_path + '"' + '"'.join(parts[1].split('"')[1:])
        processed_lines.append(line)
    
    # Unir las líneas procesadas
    formatted_exception = ''.join(processed_lines)
    
    return formatted_exception.strip()