def data(self, *keys):
    """
    Devuelve las claves y valores de este registro como un diccionario, opcionalmente incluyendo solo ciertos valores por índice o clave. Las claves proporcionadas en los elementos que no están en el registro se insertarán con un valor de :const:`None`; los índices proporcionados que están fuera de los límites generarán una excepción :exc:`IndexError`.

    :param keys: índices o claves de los elementos a incluir; si no se proporciona ninguno, se incluirán todos los valores.
    :return: diccionario de valores, indexado por el nombre del campo.  
    :raises: :exc:`IndexError` si se especifica un índice fuera de los límites.  
    """
    if not keys:
        return {key: getattr(self, key, None) for key in self.__dict__}

    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self):
                raise IndexError("Índice fuera de los límites.")
            result[key] = self[key]
        else:
            result[key] = getattr(self, key, None)

    return result