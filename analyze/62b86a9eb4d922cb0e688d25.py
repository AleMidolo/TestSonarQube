def _get_resource_name_regex():
    """
    Construye o devuelve las expresiones regulares que se utilizan para validar  
    el nombre de los recursos de Krake.

    Retorna:  
        (re.Pattern): las expresiones regulares compiladas, para validar  
        el nombre del recurso.
    """
    import re
    
    # Patrón que permite letras, números, guiones y puntos
    # Debe comenzar y terminar con alfanumérico
    # Longitud mínima 1, máxima 253 caracteres
    pattern = r'^[a-zA-Z0-9][-a-zA-Z0-9.]*[a-zA-Z0-9]$|^[a-zA-Z0-9]$'
    
    # Compilar y retornar el patrón
    return re.compile(pattern)