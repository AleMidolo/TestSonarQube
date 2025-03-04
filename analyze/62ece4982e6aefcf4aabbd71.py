def regex_dict(item):
    import re
    
    # Diccionario para almacenar resultado
    result = {}
    
    # Iterar sobre cada clave-valor del diccionario original
    for key, value in item.items():
        # Convertir comodín a regex
        # Escapar caracteres especiales
        regex_key = re.escape(key)
        # Reemplazar \* por .* para que coincida con cualquier caracter
        regex_key = regex_key.replace(r'\*', '.*')
        # Agregar ^ al inicio y $ al final para coincidencia exacta
        regex_key = f'^{regex_key}$'
        
        # Agregar al diccionario resultado
        result[regex_key] = value
        
    return result