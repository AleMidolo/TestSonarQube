def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement, BrokenImplementation, BrokenMethodImplementation
    from zope.interface.interface import Method
    
    errors = []

    # Step 1: Check if candidate declares it provides the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(DoesNotImplement(iface))

    # Step 2 & 3: Check methods
    for name, desc in iface.namesAndDescriptions(1):
        if isinstance(desc, Method):
            # Check if method exists
            try:
                attr = getattr(candidate, name)
            except AttributeError:
                errors.append(BrokenImplementation(iface, name))
                continue

            # Check if it's callable
            if not callable(attr):
                errors.append(BrokenMethodImplementation(name, "Not a method"))
                continue

            # Check method signature if possible
            try:
                from inspect import signature
                expected_sig = signature(desc)
                actual_sig = signature(attr)
                
                if expected_sig != actual_sig:
                    errors.append(BrokenMethodImplementation(
                        name,
                        f"Signature mismatch. Expected {expected_sig}, got {actual_sig}"
                    ))
            except ValueError:
                # Can't get signature, skip this check
                pass

    # Step 4: Check attributes
    for name, desc in iface.namesAndDescriptions(1):
        if not isinstance(desc, Method):
            try:
                getattr(candidate, name)
            except AttributeError:
                errors.append(BrokenImplementation(iface, name))

    # Handle errors
    if len(errors) == 1:
        raise errors[0]
    elif errors:
        raise Invalid(errors)

    return True