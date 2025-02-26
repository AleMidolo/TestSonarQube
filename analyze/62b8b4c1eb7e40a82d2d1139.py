def verifyClass(iface, candidate, tentative=False):
    """
    验证 *candidate* 是否可能正确地提供 *iface*。
    """
    if tentative:
        return issubclass(candidate, iface) or (hasattr(candidate, '__bases__') and any(issubclass(base, iface) for base in candidate.__bases__))
    else:
        return issubclass(candidate, iface)