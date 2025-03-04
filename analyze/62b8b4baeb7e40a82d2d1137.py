def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement, BrokenImplementation, BrokenMethodImplementation
    from zope.interface.interface import Method
    
    errors = []

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors.append(DoesNotImplement(iface))

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(1):
        try:
            attr = getattr(candidate, name)
        except AttributeError:
            errors.append(BrokenImplementation(iface, name))
            continue

        # If it's a method, verify the signature
        if isinstance(desc, Method):
            if not callable(attr):
                errors.append(BrokenMethodImplementation(name, desc, "Not callable"))
                continue
            
            # Check method signature using inspect
            import inspect
            try:
                method_sig = inspect.signature(attr)
                iface_sig = inspect.signature(desc)
                
                # Compare parameters
                if list(method_sig.parameters.keys()) != list(iface_sig.parameters.keys()):
                    errors.append(BrokenMethodImplementation(name, desc, "Incorrect signature"))
            except ValueError:
                # Can't get signature, skip detailed checking
                pass

    # If we have errors, raise them
    if len(errors) == 1:
        raise errors[0]
    elif errors:
        raise Invalid(errors)

    return True