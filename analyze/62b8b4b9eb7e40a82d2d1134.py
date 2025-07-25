def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    
    Args:
        all (bool): Si es True, devuelve todos los atributos. Si es False, devuelve solo los atributos definidos por la interfaz.
    
    Returns:
        dict: Un diccionario donde las claves son los nombres de los atributos y los valores son las descripciones.
    """
    attributes = {}
    for name, attr in self.__dict__.items():
        if all or not name.startswith('_'):
            attributes[name] = attr.__doc__ if attr.__doc__ else "No description available."
    return attributes