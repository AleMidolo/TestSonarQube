def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    """
    if not tentative:
        # Check if the candidate implements all methods of the interface
        for method in dir(iface):
            if callable(getattr(iface, method)) and not method.startswith('__'):
                if not hasattr(candidate, method) or not callable(getattr(candidate, method)):
                    return False
        return True
    else:
        # Tentative check: only check if the candidate has the same methods as the interface
        iface_methods = [method for method in dir(iface) if callable(getattr(iface, method)) and not method.startswith('__')]
        candidate_methods = [method for method in dir(candidate) if callable(getattr(candidate, method)) and not method.startswith('__')]
        return set(iface_methods).issubset(set(candidate_methods))