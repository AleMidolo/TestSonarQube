def names(self, all=False): # pylint:disable=redefined-builtin
    """Restituisce i nomi degli attributi definiti dall'interfaccia."""
    if not all:
        return [name for name in self._attributes.keys() if not name.startswith('_')]
    return list(self._attributes.keys())