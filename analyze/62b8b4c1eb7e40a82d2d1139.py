def verifyClass(iface, candidate, tentative=False):
    """
    Verifica que el *candidate* pueda proporcionar correctamente *iface*.
    """
    if not tentative:
        return all(hasattr(candidate, attr) and callable(getattr(candidate, attr)) for attr in dir(iface) if not attr.startswith('__'))
    else:
        return all(hasattr(candidate, attr) for attr in dir(iface) if not attr.startswith('__'))