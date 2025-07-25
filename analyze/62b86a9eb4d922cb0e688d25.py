import re

def _get_resource_name_regex():
    """
    Construye o devuelve las expresiones regulares que se utilizan para validar  
    el nombre de los recursos de Krake.

    Retorna:  
        (re.Pattern): las expresiones regulares compiladas, para validar  
        el nombre del recurso.
    """
    resource_name_pattern = r'^[a-zA-Z0-9_-]+$'
    return re.compile(resource_name_pattern)