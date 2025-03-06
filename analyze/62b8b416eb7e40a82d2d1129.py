def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres de los atributos definidos por la interfaz.
    
    Args:
        all (bool): Si es True, devuelve todos los nombres de los atributos. 
                    Si es False, devuelve solo los nombres de los atributos definidos por la interfaz.
    
    Returns:
        list: Una lista de nombres de atributos.
    """
    if not all:
        return [name for name in dir(self) if not name.startswith('_')]
    else:
        return dir(self)