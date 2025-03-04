def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from zope.interface.verify import verifyObject
    
    errors = []
    
    # Step 1: Check if candidate declares it provides the interface
    if not tentative and not iface.providedBy(candidate):
        errors.append(f"{candidate!r} does not provide interface {iface!r}")
        
    # Step 2 & 3: Check methods and their signatures
    for name, desc in iface.namesAndDescriptions(1):
        if isinstance(desc, Method):
            # Check if method exists
            try:
                attr = getattr(candidate, name)
            except AttributeError:
                errors.append(f"The {name} attribute was not provided")
                continue
                
            # Check if it's callable
            if not callable(attr):
                errors.append(f"{name} is not callable")
                continue
                
            # Check method signature if possible
            if hasattr(desc, 'getSignatureInfo'):
                sig_info = desc.getSignatureInfo()
                try:
                    verifyObject(desc, attr)
                except Invalid as e:
                    errors.append(str(e))
    
    # Step 4: Check attributes
    for name, desc in iface.namesAndDescriptions(1):
        if not isinstance(desc, Method):
            try:
                getattr(candidate, name)
            except AttributeError:
                errors.append(f"The {name} attribute was not provided")
    
    # Handle errors
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        raise Invalid(errors)
        
    return True