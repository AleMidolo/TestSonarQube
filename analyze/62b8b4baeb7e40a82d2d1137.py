def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement, BrokenImplementation, BrokenMethodImplementation
    from zope.interface.verify import verifyClass
    from zope.interface.interface import Method
    
    # Step 1: Check if candidate provides interface
    if not tentative:
        if not iface.providedBy(candidate):
            raise DoesNotImplement(iface)

    # Collect all errors
    errors = []
    
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
                if hasattr(desc, 'getSignatureInfo'):
                    expected = desc.getSignatureInfo()
                    actual = Method(attr).getSignatureInfo()
                    if expected != actual:
                        errors.append(BrokenMethodImplementation(name, "Incorrect signature"))
            except ValueError:
                pass  # Can't check signature
    
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