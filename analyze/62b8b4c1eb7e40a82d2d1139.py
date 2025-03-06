def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    """
    if not all(hasattr(candidate, method) for method in dir(iface) if callable(getattr(iface, method))):
        return False
    if tentative:
        return True
    try:
        instance = candidate()
        for method in dir(iface):
            if callable(getattr(iface, method)):
                getattr(instance, method)()
        return True
    except Exception:
        return False