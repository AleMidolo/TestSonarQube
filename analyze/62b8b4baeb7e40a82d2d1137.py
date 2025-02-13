def verifyObject(iface, candidate, tentative=False):
    from zope.interface import providedBy, Invalid
    from inspect import signature, isfunction

    errors = []

    if not tentative and not providedBy(candidate).isOrExtends(iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = iface.names()
    for method_name, method in required_methods:
        if not hasattr(candidate, method_name):
            errors.append(f"{candidate} is missing method {method_name}")
            continue
        
        candidate_method = getattr(candidate, method_name)
        if not isfunction(candidate_method):
            errors.append(f"{candidate}.{method_name} is not a method")
            continue
        
        iface_signature = signature(method)
        candidate_signature = signature(candidate_method)
        if iface_signature != candidate_signature:
            errors.append(f"{candidate}.{method_name} has incorrect signature")

    required_attributes = iface.names()
    for attr_name, _ in required_attributes:
        if not hasattr(candidate, attr_name):
            errors.append(f"{candidate} is missing attribute {attr_name}")

    if errors:
        raise Invalid(errors)

    return True