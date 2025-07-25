def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement, BrokenImplementation, BrokenMethodImplementation
    from zope.interface.verify import verifyClass
    from zope.interface.interface import Method
    
    # Step 1: Check if candidate provides interface (skip if tentative)
    if not tentative:
        if not iface.providedBy(candidate):
            raise DoesNotImplement(iface)

    # Collect all errors
    errors = []
    
    # Step 2 & 3: Check methods - existence and signature
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
                if not desc.validateSignature(attr):
                    errors.append(BrokenMethodImplementation(name, "Incorrect method signature"))
            except ValueError:
                # If we can't validate signature, we skip it
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
        raise Invalid("Multiple implementation errors", errors)

    return True