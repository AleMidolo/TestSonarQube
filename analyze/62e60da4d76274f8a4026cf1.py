def values(self, *keys):
    """
    Devuelve los valores del registro, filtrando opcionalmente para incluir solo ciertos valores por índice o clave.

    :param keys: índices o claves de los elementos a incluir; si no se proporcionan, se incluirán todos los valores  
    :return: lista de valores  
    :rtype: list
    """
    if not keys:
        return list(self.data.values())
    return [self.data[key] for key in keys if key in self.data]