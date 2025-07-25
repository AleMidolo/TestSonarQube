def verifyClass(iface, candidate, tentative=False):
    """
    Verify that the *candidate* might correctly provide *iface*.
    """
    if tentative:
        return issubclass(candidate, iface) or (hasattr(candidate, '__mro__') and iface in candidate.__mro__)
    return isinstance(candidate, iface)