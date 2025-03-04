def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    """
    if tentative:
        return issubclass(candidate, iface)
    
    return all(hasattr(candidate, method) for method in dir(iface) if callable(getattr(iface, method))) and issubclass(candidate, iface)