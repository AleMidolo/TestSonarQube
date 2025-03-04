def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Restituisce i nomi e le descrizioni degli attributi definiti dall'interfaccia."""
    if not all:
        return {attr: desc for attr, desc in self.interface_attributes.items() if not desc.hidden}
    return {attr: desc for attr, desc in self.interface_attributes.items()}