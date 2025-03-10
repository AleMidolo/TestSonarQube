def verifyClass(iface, candidate, tentative=False):
    """
    Verifica che il *candidate* possa fornire correttamente *iface*.
    """
    if not tentative:
        # Check if the candidate implements all methods of the interface
        for method in dir(iface):
            if not method.startswith('__'):
                if not hasattr(candidate, method):
                    return False
        return True
    else:
        # Tentative check: only check if the candidate has at least one method of the interface
        for method in dir(iface):
            if not method.startswith('__'):
                if hasattr(candidate, method):
                    return True
        return False