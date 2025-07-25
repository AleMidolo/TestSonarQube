def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    """
    if not all(hasattr(candidate, attr) for attr in dir(iface) if not attr.startswith('__'):
        return False
    if not tentative:
        for attr in dir(iface):
            if not attr.startswith('__'):
                iface_attr = getattr(iface, attr)
                candidate_attr = getattr(candidate, attr)
                if not callable(iface_attr) and iface_attr != candidate_attr:
                    return False
                if callable(iface_attr) and not callable(candidate_attr):
                    return False
    return True