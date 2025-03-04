def difference(d1, d2, level=-1):
    """
    Devuelve un diccionario con los elementos de *d1* que no están contenidos en *d2*.

    El parámetro *level* establece la profundidad máxima de recursión. Para recursión infinita, configúralo en -1. Para un nivel 1, si una clave está presente tanto en *d1* como en *d2* pero tiene valores diferentes, se incluye en la diferencia. Consulta :func:`intersection` para más detalles.

    *d1* y *d2* permanecen sin cambios. Sin embargo, *d1* o algunos de sus subdiccionarios pueden ser devueltos directamente. Realiza una copia profunda del resultado cuando sea apropiado.

    .. versionadded:: 0.5  
       Agrega el argumento de palabra clave *level*.
    """
    result = {}
    
    # Iterar sobre todas las claves en d1
    for key in d1:
        # Si la clave no está en d2, incluir el valor completo de d1
        if key not in d2:
            result[key] = d1[key]
        # Si level no es 0 y ambos valores son diccionarios, hacer recursión
        elif level != 0 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
            nested = difference(d1[key], d2[key], level - 1 if level > 0 else -1)
            if nested:
                result[key] = nested
        # Si los valores son diferentes y estamos en nivel 1 o superior
        elif d1[key] != d2[key]:
            result[key] = d1[key]
            
    return result