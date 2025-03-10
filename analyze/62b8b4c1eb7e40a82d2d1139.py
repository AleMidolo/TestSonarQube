def verifyClass(iface, candidate, tentative=False):
    """
    Verifica que el *candidate* pueda proporcionar correctamente *iface*.
    """
    if not tentative:
        return issubclass(candidate, iface)
    else:
        try:
            return issubclass(candidate, iface)
        except TypeError:
            return False