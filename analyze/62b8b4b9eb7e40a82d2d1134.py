def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres y descripciones de los atributos definidos por la interfaz.
    
    Args:
        all (bool): Si es True, devuelve todos los atributos. Si es False, devuelve solo los atributos definidos por la interfaz.
    
    Returns:
        dict: Un diccionario donde las claves son los nombres de los atributos y los valores son las descripciones.
    """
    attributes = self.__dict__
    if not all:
        attributes = {k: v for k, v in attributes.items() if not k.startswith('_')}
    
    descriptions = {k: v.__doc__ for k, v in attributes.items() if v.__doc__}
    return descriptions