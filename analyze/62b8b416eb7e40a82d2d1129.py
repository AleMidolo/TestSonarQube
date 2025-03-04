def names(self, all=False): # pylint:disable=redefined-builtin
    """Restituisce i nomi degli attributi definiti dall'interfaccia."""
    if not all:
        return [attr for attr in dir(self) if not attr.startswith('_')]
    return dir(self)