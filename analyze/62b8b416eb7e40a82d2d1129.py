def names(self, all=False): # pylint:disable=redefined-builtin
    """Restituisce i nomi degli attributi definiti dall'interfaccia."""
    if not all:
        return [name for name in self.__dict__ if not name.startswith('_')]
    return list(self.__dict__.keys())