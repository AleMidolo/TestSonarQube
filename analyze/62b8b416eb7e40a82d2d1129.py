def names(self, all=False):  # pylint:disable=redefined-builtin
    """Restituisce i nomi degli attributi definiti dall'interfaccia."""
    if not all:
        return [name for name in dir(self) if not name.startswith('_')]
    else:
        return [name for name in dir(self)]