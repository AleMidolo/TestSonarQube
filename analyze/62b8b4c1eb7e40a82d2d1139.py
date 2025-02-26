def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    """
    if tentative:
        return issubclass(candidate, iface) or iface in candidate.__bases__
    return issubclass(candidate, iface)