def verifyObject(iface, candidate, tentative=False):
    from zope.interface.exceptions import Invalid, DoesNotImplement, BrokenImplementation, BrokenMethodImplementation
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate provides interface
    if not tentative and not iface.providedBy(candidate):
        raise DoesNotImplement(iface)

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(1):
        try:
            attr = getattr(candidate, name, None)
            if attr is None:
                errors['missing'].append(name)
                continue

            # Verify methods
            if isinstance(desc, Method):
                # Check if callable
                if not callable(attr):
                    errors['not_callable'].append(name)
                    continue

                # Check method signature
                try:
                    from inspect import signature
                    method_sig = signature(attr)
                    iface_sig = signature(desc)
                    
                    if method_sig != iface_sig:
                        errors['wrong_signature'].append(name)
                
                except ValueError:
                    # Can't get signature, skip check
                    pass

        except Exception as e:
            errors['error'].append((name, str(e)))

    # Handle errors
    if not errors:
        return True

    # Collect all error messages
    error_msgs = []
    if errors['missing']:
        error_msgs.append(f"Missing attributes: {', '.join(errors['missing'])}")
    if errors['not_callable']:
        error_msgs.append(f"Attributes that should be methods: {', '.join(errors['not_callable'])}")
    if errors['wrong_signature']:
        error_msgs.append(f"Methods with wrong signatures: {', '.join(errors['wrong_signature'])}")
    if errors['error']:
        error_msgs.extend(f"Error checking {name}: {msg}" for name, msg in errors['error'])

    # If single error, raise directly
    if len(error_msgs) == 1:
        raise BrokenImplementation(iface, error_msgs[0])

    # Multiple errors
    raise Invalid("\n".join(error_msgs))