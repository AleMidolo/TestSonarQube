def names(self, all=False):  # pylint:disable=redefined-builtin
    """
    Devuelve los nombres de los atributos definidos por la interfaz.
    if not all:

    Devuelve los nombres de los atributos definidos por la interfaz.
    """
    if all:
        return [attr for attr in dir(self) if not attr.startswith('_')]
    else:
        return [attr for attr in dir(self) if not attr.startswith('_') and not callable(getattr(self, attr))]