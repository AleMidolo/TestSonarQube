import re

def _get_resource_name_regex():
    """
    Construye o devuelve las expresiones regulares que se utilizan para validar  
    el nombre de los recursos de Krake.

    Retorna:  
        (re.Pattern): las expresiones regulares compiladas, para validar  
        el nombre del recurso.
    """
    # Expresión regular que permite letras minúsculas, números, guiones y puntos.
    # El nombre debe comenzar con una letra y terminar con una letra o número.
    # La longitud mínima es 1 y la máxima es 253 caracteres.
    pattern = r'^[a-z]([a-z0-9\-\.]*[a-z0-9])?$'
    return re.compile(pattern)