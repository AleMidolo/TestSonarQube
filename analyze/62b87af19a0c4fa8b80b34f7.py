def difference(d1, d2, level=-1):
    """
    Devuelve un diccionario con los elementos de *d1* que no están contenidos en *d2*.

    El parámetro *level* establece la profundidad máxima de recursión. Para recursión infinita, configúralo en -1. Para un nivel 1, si una clave está presente tanto en *d1* como en *d2* pero tiene valores diferentes, se incluye en la diferencia. Consulta :func:`intersection` para más detalles.

    *d1* y *d2* permanecen sin cambios. Sin embargo, *d1* o algunos de sus subdiccionarios pueden ser devueltos directamente. Realiza una copia profunda del resultado cuando sea apropiado.

    .. versionadded:: 0.5  
       Agrega el argumento de palabra clave *level*.
    """
    if level == 0:
        return {k: v for k, v in d1.items() if k not in d2 or d2[k] != v}
    
    diff = {}
    for k, v in d1.items():
        if k not in d2:
            diff[k] = v
        elif isinstance(v, dict) and isinstance(d2[k], dict) and level != 0:
            sub_diff = difference(v, d2[k], level - 1 if level != -1 else -1)
            if sub_diff:
                diff[k] = sub_diff
        elif v != d2[k]:
            diff[k] = v
    return diff