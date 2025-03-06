def data(self, *keys):
    """
    Devuelve las claves y valores de este registro como un diccionario, opcionalmente incluyendo solo ciertos valores por índice o clave. Las claves proporcionadas en los elementos que no están en el registro se insertarán con un valor de :const:`None`; los índices proporcionados que están fuera de los límites generarán una excepción :exc:`IndexError`.

    :param keys: índices o claves de los elementos a incluir; si no se proporciona ninguno, se incluirán todos los valores.
    :return: diccionario de valores, indexado por el nombre del campo.  
    :raises: :exc:`IndexError` si se especifica un índice fuera de los límites.  
    """
    # Asumimos que self._fields contiene las claves y self._values los valores correspondientes
    if not keys:
        return dict(zip(self._fields, self._values))
    
    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self._values):
                raise IndexError("Índice fuera de los límites")
            result[self._fields[key]] = self._values[key]
        else:
            if key in self._fields:
                index = self._fields.index(key)
                result[key] = self._values[index]
            else:
                result[key] = None
    return result