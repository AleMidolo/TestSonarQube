def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    if not tentative:
        return issubclass(candidate, iface)
    else:
        try:
            return issubclass(candidate, iface)
        except TypeError:
            return False