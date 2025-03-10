def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres de los atributos definidos por la interfaz.
    
    Args:
        all (bool): Si es True, devuelve todos los atributos, incluyendo los privados.
                    Si es False, devuelve solo los atributos públicos.
    
    Returns:
        list: Una lista de nombres de atributos.
    """
    if all:
        return [attr for attr in dir(self) if not callable(getattr(self, attr))]
    else:
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith('_')]