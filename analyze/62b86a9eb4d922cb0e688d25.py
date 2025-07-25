import re

def _get_resource_name_regex():
    """
    Construye o devuelve las expresiones regulares que se utilizan para validar  
    el nombre de los recursos de Krake.

    Retorna:  
        (re.Pattern): las expresiones regulares compiladas, para validar  
        el nombre del recurso.
    """
    # Define la expresión regular para validar nombres de recursos
    # Ejemplo: permite letras, números, guiones y guiones bajos, con una longitud mínima de 1
    resource_name_pattern = r'^[a-zA-Z0-9_-]+$'
    
    # Compila la expresión regular
    return re.compile(resource_name_pattern)