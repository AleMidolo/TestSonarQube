def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    """
    if not all(hasattr(candidate, method) for method in dir(iface) if not method.startswith('__')):
        return False
    if not tentative:
        for method in dir(iface):
            if not method.startswith('__'):
                iface_method = getattr(iface, method)
                candidate_method = getattr(candidate, method)
                if not callable(iface_method) or not callable(candidate_method):
                    return False
    return True