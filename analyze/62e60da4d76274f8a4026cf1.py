def values(self, *keys):
    """
    Devuelve los valores del registro, filtrando opcionalmente para incluir solo ciertos valores por índice o clave.

    :param keys: índices o claves de los elementos a incluir; si no se proporcionan, se incluirán todos los valores  
    :return: lista de valores  
    :rtype: list
    """
    if not keys:
        # Si no se proporcionan keys, devolver todos los valores
        return list(self._data.values())
    
    result = []
    for key in keys:
        if isinstance(key, int):
            # Si la key es un índice numérico
            if 0 <= key < len(self._data):
                # Obtener el valor en esa posición
                result.append(list(self._data.values())[key])
        else:
            # Si la key es una clave del diccionario
            if key in self._data:
                result.append(self._data[key])
                
    return result