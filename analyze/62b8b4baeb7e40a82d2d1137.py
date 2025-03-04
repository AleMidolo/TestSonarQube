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
        # Check if attribute exists
        try:
            attr = getattr(candidate, name)
        except AttributeError:
            errors.append(Invalid(f"The object is missing attribute '{name}' required by {iface.__name__}"))
            continue

        # If it's a method, verify the signature
        if isinstance(desc, Method):
            # Get method signature
            try:
                import inspect
                method_sig = inspect.signature(attr)
                iface_sig = inspect.signature(desc.interface[name])
                
                # Compare signatures
                if str(method_sig) != str(iface_sig):
                    errors.append(Invalid(
                        f"Method '{name}' has wrong signature. "
                        f"Expected {str(iface_sig)}, got {str(method_sig)}"
                    ))
            except (ValueError, TypeError):
                # Can't get signature, skip verification
                pass

    # If there are multiple errors, raise them all together
    if len(errors) > 1:
        raise Invalid(errors)
    # If there's exactly one error, raise it directly
    elif len(errors) == 1:
        raise errors[0]
    
    return True