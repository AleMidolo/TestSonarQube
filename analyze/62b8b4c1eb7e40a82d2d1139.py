def verifyClass(iface, candidate, tentative=False):
    """
    验证 *candidate* 是否可能正确地提供 *iface*。
    """
    if tentative:
        return issubclass(candidate, iface) or iface in candidate.__bases__
    return isinstance(candidate, iface)