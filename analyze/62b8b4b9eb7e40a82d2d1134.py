def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Restituisce i nomi e le descrizioni degli attributi definiti dall'interfaccia."""
    if not all:
        return [(name, desc) for name, desc in self._attributes.items() if not name.startswith('_')]
    else:
        return [(name, desc) for name, desc in self._attributes.items()]