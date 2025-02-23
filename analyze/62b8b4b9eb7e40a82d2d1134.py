def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Restituisce i nomi e le descrizioni degli attributi definiti dall'interfaccia."""
    if not all:
        return {attr: desc for attr, desc in self.get_attributes().items() if self.is_defined(attr)}
    else:
        return {attr: desc for attr, desc in self.get_attributes().items()}