def verifyClass(iface, candidate, tentative=False):
    """
    Verifica que el *candidate* pueda proporcionar correctamente *iface*.
    """
    if not all(hasattr(candidate, attr) for attr in dir(iface) if not tentative else True:
        return False
    return True