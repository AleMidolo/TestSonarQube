def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid, DoesNotImplement
    from zope.interface.verify import verifyObject
    from zope.interface.interface import Method
    
    errors = []

    # Step 1: Check if candidate declares it provides the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(DoesNotImplement(iface))

    # Step 2 & 3: Check methods and their signatures
    for name, desc in iface.namesAndDescriptions(1):
        if isinstance(desc, Method):
            # Check if method exists
            try:
                attr = getattr(candidate, name)
            except AttributeError:
                errors.append(Invalid(f"The '{name}' attribute was not provided."))
                continue

            # Verify it's callable
            if not callable(attr):
                errors.append(Invalid(f"The '{name}' attribute is not callable."))
                continue

            # Check method signature if possible
            try:
                if hasattr(desc, 'getSignatureInfo'):
                    sig_info = desc.getSignatureInfo()
                    method_sig = verifyObject(sig_info, attr)
                    if not method_sig:
                        errors.append(Invalid(f"The '{name}' method has an invalid signature."))
            except Exception as e:
                errors.append(Invalid(f"Error verifying signature of '{name}': {str(e)}"))

    # Step 4: Check attributes
    for name, desc in iface.namesAndDescriptions(1):
        if not isinstance(desc, Method):
            try:
                getattr(candidate, name)
            except AttributeError:
                errors.append(Invalid(f"The '{name}' attribute was not provided."))

    # Handle errors
    if len(errors) == 0:
        return True
    elif len(errors) == 1:
        raise errors[0]
    else:
        raise Invalid(f"Multiple errors: {'; '.join(str(e) for e in errors)}")