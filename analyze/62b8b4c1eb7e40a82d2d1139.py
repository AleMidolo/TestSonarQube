def verifyClass(iface, candidate, tentative=False):
    """
    验证 *candidate* 是否可能正确地提供 *iface*。
    """
    if not hasattr(candidate, '__bases__'):
        return False
    
    if iface in candidate.__bases__:
        return True
    
    if tentative:
        for base in candidate.__bases__:
            if verifyClass(iface, base, tentative):
                return True
    
    return False