def pop(self, key, default=__marker):
    """
    D.pop(k[,d]) -> v, elimina la clave especificada y devuelve el valor correspondiente.
    Si la clave no se encuentra, se devuelve `d` si se proporciona; de lo contrario, se genera una excepción KeyError.
    """
    if key in self:
        value = self[key]
        del self[key]
        return value
    elif default is not __marker:
        return default
    else:
        raise KeyError(f"KeyError: {key}")