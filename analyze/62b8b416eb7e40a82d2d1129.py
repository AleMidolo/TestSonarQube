def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres de los atributos definidos por la interfaz.
    if not all:

    Devuelve los nombres de los atributos definidos por la interfaz.
    """
    if all:
        return list(self._attributes.keys())
    else:
        return [name for name, attr in self._attributes.items() 
                if not attr.get('system', False)]