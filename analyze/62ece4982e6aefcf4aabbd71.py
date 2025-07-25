def regex_dict(item):
    """
    Convertir claves `*.cpp` a claves de expresiones regulares.

    Dado un diccionario donde las claves son nombres de archivo con comodines, convierte únicamente las claves en expresiones regulares equivalentes y deja los valores intactos.

    Ejemplo
    rules = {
        '*.cpp': {'a': 'arf', 'b': 'bark', 'c': 'coo'},
        '*.h': {'h': 'help'}
    }

    regex_keys = regex_dict(rules)

    Argumentos:
        item (dict): Diccionario a convertir.

    Retorno:
        dict: Diccionario con claves convertidas a expresiones regulares.
    """
    import re
    
    # Crear nuevo diccionario para almacenar resultado
    result = {}
    
    # Iterar sobre cada clave-valor del diccionario original
    for key, value in item.items():
        # Escapar caracteres especiales excepto *
        escaped_key = re.escape(key).replace('\\*', '.*')
        # Agregar ^ al inicio y $ al final para match completo
        regex_key = f'^{escaped_key}$'
        # Agregar al diccionario resultado
        result[regex_key] = value
        
    return result