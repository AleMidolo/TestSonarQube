def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from zope.interface.verify import verifyObject
    
    errors = []
    
    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors.append(f"{candidate} does not provide interface {iface}")
        
    # Check required methods
    for name, desc in iface.namesAndDescriptions(1):
        if isinstance(desc, Method):
            # Check if method exists
            try:
                attr = getattr(candidate, name)
            except AttributeError:
                errors.append(f"Method {name} not provided by {candidate}")
                continue
                
            # Check if it's callable
            if not callable(attr):
                errors.append(f"Attribute {name} is not callable on {candidate}")
                continue
                
            # Verify method signature if possible
            try:
                verifyObject(desc, attr, name)
            except Invalid as e:
                errors.append(str(e))
        
        else:
            # Check required attributes
            try:
                getattr(candidate, name)
            except AttributeError:
                errors.append(f"Attribute {name} not provided by {candidate}")
    
    # If there are errors, raise them
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        raise Invalid(errors)
        
    return True