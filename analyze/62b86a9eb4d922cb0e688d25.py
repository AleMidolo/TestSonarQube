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
    # El nombre debe comenzar con una letra minúscula y terminar con una letra minúscula o número.
    resource_name_pattern = re.compile(r'^[a-z][a-z0-9-.]*[a-z0-9]$')
    return resource_name_pattern