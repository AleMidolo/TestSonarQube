def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface import providedBy, Invalid
    from inspect import signature, isfunction

    errors = []

    if not tentative and not providedBy(candidate).provides(iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = iface.names()
    for method_name in required_methods:
        if not hasattr(candidate, method_name):
            errors.append(f"{candidate} is missing method {method_name}")
            continue
        
        method = getattr(candidate, method_name)
        if not isfunction(method):
            errors.append(f"{method_name} in {candidate} is not a function")
            continue
        
        expected_signature = signature(getattr(iface, method_name))
        actual_signature = signature(method)
        if expected_signature != actual_signature:
            errors.append(f"Signature mismatch for {method_name} in {candidate}")

    required_attributes = iface.attributes()
    for attr_name in required_attributes:
        if not hasattr(candidate, attr_name):
            errors.append(f"{candidate} is missing attribute {attr_name}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        raise Invalid(errors)

    return True