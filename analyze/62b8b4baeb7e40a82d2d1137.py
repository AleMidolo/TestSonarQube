def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement, BrokenImplementation, BrokenMethodImplementation
    from zope.interface.interface import Method
    
    errors = []

    # Check if candidate provides interface (unless tentative)
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(DoesNotImplement(iface))

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(1):
        try:
            attr = getattr(candidate, name, None)
            if attr is None:
                errors.append(BrokenImplementation(iface, name))
                continue

            # If it's a method, verify the signature
            if isinstance(desc, Method):
                if not callable(attr):
                    errors.append(BrokenMethodImplementation(name, "Not callable"))
                    continue
                
                # Check method signature
                try:
                    from inspect import signature
                    method_sig = signature(attr)
                    interface_sig = signature(desc)
                    
                    # Compare parameters
                    if str(method_sig) != str(interface_sig):
                        errors.append(BrokenMethodImplementation(name, 
                            f"Signature mismatch. Expected {interface_sig}, got {method_sig}"))
                except ValueError:
                    # Can't get signature, skip detailed checking
                    pass

        except Exception as e:
            errors.append(BrokenImplementation(iface, name, str(e)))

    # Handle errors
    if len(errors) == 0:
        return True
    elif len(errors) == 1:
        raise errors[0]
    else:
        raise Invalid(errors)