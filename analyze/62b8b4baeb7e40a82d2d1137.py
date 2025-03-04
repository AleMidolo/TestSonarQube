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
                errors.append(BrokenMethodImplementation(name, "Not callable"))
                continue
                
            # Check method signature
            try:
                desc.getSignatureInfo()
            except ValueError as e:
                errors.append(BrokenMethodImplementation(name, str(e)))

    # If no errors, return True
    if not errors:
        return True
        
    # If only one error, raise it directly
    if len(errors) == 1:
        raise errors[0]
        
    # If multiple errors, raise Invalid with all errors
    if errors:
        raise Invalid(errors)

    return True