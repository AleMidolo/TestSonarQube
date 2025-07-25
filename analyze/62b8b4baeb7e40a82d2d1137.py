def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement
    from zope.interface.verify import verifyClass
    from zope.interface.interface import Method
    
    errors = []

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors.append(DoesNotImplement(iface))

    # Get all attributes defined by the interface
    for name, desc in iface.namesAndDescriptions(1):
        # Skip if attribute doesn't exist
        if not hasattr(candidate, name):
            errors.append(Invalid(f"The object is missing attribute '{name}' from interface {iface.__name__}"))
            continue

        attr = getattr(candidate, name)
        
        # If it's a method, verify the signature
        if isinstance(desc, Method):
            # Get method object
            if not callable(attr):
                errors.append(Invalid(f"'{name}' is not callable but interface {iface.__name__} defines it as a method"))
                continue

            # Verify method signature
            try:
                from inspect import signature
                method_sig = signature(attr)
                interface_sig = signature(desc)
                
                # Compare parameters
                if str(method_sig) != str(interface_sig):
                    errors.append(Invalid(
                        f"Method '{name}' signature {method_sig} does not match interface signature {interface_sig}"
                    ))
            except ValueError:
                # Can't get signature, skip verification
                pass

    # If we have errors, raise them
    if errors:
        if len(errors) == 1:
            raise errors[0]
        raise Invalid(
            f"The object failed to implement interface {iface.__name__}: " + 
            "; ".join(str(e) for e in errors)
        )

    return True