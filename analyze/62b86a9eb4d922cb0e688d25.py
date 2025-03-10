import re

def _get_resource_name_regex():
    """
    Construye o devuelve las expresiones regulares que se utilizan para validar
    el nombre de los recursos de Krake.

    Retorna:
        (re.Pattern): las expresiones regulares compiladas, para validar
        el nombre del recurso.
    """
    # Expresión regular que permite letras, números, guiones y guiones bajos
    # con una longitud mínima de 1 y máxima de 63 caracteres.
    pattern = r'^[a-zA-Z0-9_-]{1,63}$'
    return re.compile(pattern)