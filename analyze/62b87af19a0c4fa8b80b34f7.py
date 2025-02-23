def difference(d1, d2, level=-1):
    """
    Devuelve un diccionario con los elementos de *d1* que no están contenidos en *d2*.

    El parámetro *level* establece la profundidad máxima de recursión. Para recursión infinita, configúralo en -1. Para un nivel 1, si una clave está presente tanto en *d1* como en *d2* pero tiene valores diferentes, se incluye en la diferencia. Consulta :func:`intersection` para más detalles.

    *d1* y *d2* permanecen sin cambios. Sin embargo, *d1* o algunos de sus subdiccionarios pueden ser devueltos directamente. Realiza una copia profunda del resultado cuando sea apropiado.

    .. versionadded:: 0.5  
       Agrega el argumento de palabra clave *level*.
    """
    from collections.abc import MutableMapping
    import copy

    def recursive_difference(d1, d2, level):
        if level == 0:
            return {}
        
        result = {}
        for key, value in d1.items():
            if key not in d2:
                result[key] = copy.deepcopy(value)
            else:
                if isinstance(value, MutableMapping) and isinstance(d2[key], MutableMapping):
                    nested_diff = recursive_difference(value, d2[key], level - 1 if level > 0 else -1)
                    if nested_diff:
                        result[key] = nested_diff
                elif value != d2[key]:
                    result[key] = copy.deepcopy(value)
        
        return result

    return recursive_difference(d1, d2, level)