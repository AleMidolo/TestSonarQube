def difference(d1, d2, level=-1):
    """
    Devuelve un diccionario con los elementos de *d1* que no están contenidos en *d2*.

    El parámetro *level* establece la profundidad máxima de recursión. Para recursión infinita, configúralo en -1. Para un nivel 1, si una clave está presente tanto en *d1* como en *d2* pero tiene valores diferentes, se incluye en la diferencia. Consulta :func:`intersection` para más detalles.

    *d1* y *d2* permanecen sin cambios. Sin embargo, *d1* o algunos de sus subdiccionarios pueden ser devueltos directamente. Realiza una copia profunda del resultado cuando sea apropiado.

    .. versionadded:: 0.5  
       Agrega el argumento de palabra clave *level*.
    """
    if level == 0:
        return {}
    
    diff = {}
    for key, value in d1.items():
        if key not in d2:
            diff[key] = value
        elif isinstance(value, dict) and isinstance(d2[key], dict):
            if level != -1:
                sub_diff = difference(value, d2[key], level - 1)
            else:
                sub_diff = difference(value, d2[key], level)
            if sub_diff:
                diff[key] = sub_diff
        elif value != d2[key]:
            diff[key] = value
    
    return diff