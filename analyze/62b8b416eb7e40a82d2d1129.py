def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres de los atributos definidos por la interfaz.
    if not all:

    Devuelve los nombres de los atributos definidos por la interfaz.
    """
    if all:
        # Return all attribute names including inherited ones
        return list(self.__dict__.keys())
    else:
        # Return only directly defined attribute names
        return [name for name in self.__dict__.keys() 
                if not name.startswith('_')]