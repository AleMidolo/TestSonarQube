def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors['provide'].append(
            f"Class {candidate} does not provide interface {iface.__name__}"
        )

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            # Check if method exists
            if not hasattr(candidate, name):
                errors['methods'].append(
                    f"Method '{name}' not implemented"
                )
                continue

            method = getattr(candidate, name)
            if not callable(method):
                errors['methods'].append(
                    f"Attribute '{name}' is not callable"
                )
                continue

            # Check method signature
            try:
                from inspect import signature
                impl_sig = signature(method)
                iface_sig = signature(desc)
                
                if impl_sig.parameters != iface_sig.parameters:
                    errors['signatures'].append(
                        f"Method '{name}' has wrong signature: {impl_sig} != {iface_sig}"
                    )
            except ValueError:
                # Can't get signature, skip check
                pass

        else:
            # Check if attribute exists
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"Attribute '{name}' not provided"
                )

    # If no errors, return True
    if not errors:
        return True

    # If single error, raise it directly
    total_errors = sum(len(errs) for errs in errors.values())
    if total_errors == 1:
        for error_list in errors.values():
            if error_list:
                raise Invalid(error_list[0])

    # Multiple errors - raise all of them
    if errors:
        error_msg = []
        for category, msgs in errors.items():
            if msgs:
                error_msg.extend(msgs)
        raise Invalid("\n".join(error_msg))

    return True