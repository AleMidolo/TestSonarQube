def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface import providedBy, Invalid
    from inspect import signature, Parameter

    if not tentative and not providedBy(candidate).isOrExtends(iface):
        raise Invalid(f"{candidate} does not provide {iface}")

    required_methods = iface.names()
    errors = []

    for method_name in required_methods:
        if method_name not in candidate.__dict__:
            errors.append(f"Missing method: {method_name}")
            continue

        method = getattr(candidate, method_name)
        if not callable(method):
            errors.append(f"{method_name} is not callable")
            continue

        sig = signature(method)
        iface_sig = signature(iface[method_name])

        if len(sig.parameters) != len(iface_sig.parameters):
            errors.append(f"Method {method_name} has incorrect number of parameters")
            continue

        for param in iface_sig.parameters:
            if param not in sig.parameters:
                errors.append(f"Method {method_name} is missing parameter: {param}")
                continue

            if iface_sig.parameters[param].default != Parameter.empty and \
               sig.parameters[param].default == Parameter.empty:
                errors.append(f"Method {method_name} is missing default for parameter: {param}")

    required_attributes = [attr for attr in iface.names() if not callable(getattr(iface, attr))]
    
    for attr in required_attributes:
        if not hasattr(candidate, attr):
            errors.append(f"Missing attribute: {attr}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        raise Invalid(errors)

    return True