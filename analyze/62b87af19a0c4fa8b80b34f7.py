def difference(d1, d2, level=-1):
    """
    Devuelve un diccionario con los elementos de *d1* que no están contenidos en *d2*.

    El parámetro *level* establece la profundidad máxima de recursión. Para recursión infinita, configúralo en -1. Para un nivel 1, si una clave está presente tanto en *d1* como en *d2* pero tiene valores diferentes, se incluye en la diferencia. Consulta :func:`intersection` para más detalles.

    *d1* y *d2* permanecen sin cambios. Sin embargo, *d1* o algunos de sus subdiccionarios pueden ser devueltos directamente. Realiza una copia profunda del resultado cuando sea apropiado.

    .. versionadded:: 0.5  
       Agrega el argumento de palabra clave *level*.
    """
    result = {}
    
    # Iterate through all keys in d1
    for key in d1:
        # If key not in d2, include it in result
        if key not in d2:
            result[key] = d1[key]
        # If key in d2 but we can still recurse
        elif level != 0 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
            # Recursively find differences in nested dictionaries
            diff = difference(d1[key], d2[key], level - 1 if level > 0 else -1)
            if diff:
                result[key] = diff
        # If values are different at level 1 or above
        elif d1[key] != d2[key]:
            result[key] = d1[key]
            
    return result