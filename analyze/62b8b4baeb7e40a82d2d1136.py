def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors['provide'].append(
            f"{candidate} does not provide interface {iface.__name__}"
        )

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            # Check if method exists
            if not hasattr(candidate, name):
                errors['methods'].append(
                    f"Method {name} not provided by {candidate}"
                )
                continue

            method = getattr(candidate, name)
            if not callable(method):
                errors['methods'].append(
                    f"{name} is not callable on {candidate}"
                )
                continue

            # Check method signature
            try:
                from inspect import signature
                impl_sig = signature(method)
                iface_sig = signature(desc)
                
                if impl_sig.parameters != iface_sig.parameters:
                    errors['signatures'].append(
                        f"Method {name} has wrong signature: {impl_sig} != {iface_sig}"
                    )
            except ValueError:
                # Can't get signature, skip check
                pass

        else:
            # Check if attribute exists
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"Attribute {name} not provided by {candidate}"
                )

    # If no errors, return True
    if not errors:
        return True

    # If single error, raise it directly
    total_errors = sum(len(errs) for errs in errors.values())
    if total_errors == 1:
        for err_list in errors.values():
            if err_list:
                raise Invalid(err_list[0])

    # Multiple errors - raise all of them
    if errors:
        error_msg = []
        for category, err_list in errors.items():
            if err_list:
                error_msg.extend(err_list)
        raise Invalid("\n".join(error_msg))

    return True