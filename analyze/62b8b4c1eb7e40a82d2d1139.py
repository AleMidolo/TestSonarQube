def verifyClass(iface, candidate, tentative=False):
    """
    Verifica que el *candidate* pueda proporcionar correctamente *iface*.
    """
    if tentative:
        return issubclass(candidate, iface) or (hasattr(candidate, '__bases__') and any(issubclass(base, iface) for base in candidate.__bases__))
    return issubclass(candidate, iface)