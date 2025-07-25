def verifyClass(iface, candidate, tentative=False):
    """
    Verifica que el *candidate* pueda proporcionar correctamente *iface*.
    """
    if tentative:
        return issubclass(candidate, iface) or (hasattr(candidate, '__mro__') and iface in candidate.__mro__)
    return isinstance(candidate, iface) or (hasattr(candidate, '__mro__') and iface in candidate.__mro__)