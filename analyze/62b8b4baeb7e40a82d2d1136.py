def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors['general'].append(
            f"Class {candidate} does not implement interface {iface.__name__}"
        )

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            # Check if method exists
            if not hasattr(candidate, name):
                errors['methods'].append(
                    f"Method '{name}' not provided by {candidate}"
                )
                continue

            method = getattr(candidate, name)
            if not callable(method):
                errors['methods'].append(
                    f"Attribute '{name}' is not callable as required"
                )
                continue

            # Check method signature if possible
            try:
                import inspect
                impl_sig = inspect.signature(method)
                iface_sig = inspect.signature(desc)
                
                if impl_sig.parameters != iface_sig.parameters:
                    errors['signatures'].append(
                        f"Method '{name}' has incorrect signature: {impl_sig} != {iface_sig}"
                    )
            except (ValueError, TypeError):
                pass  # Skip signature checking if not possible

        else:
            # Check if attribute exists
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"Attribute '{name}' not provided by {candidate}"
                )

    # If no errors, return True
    if not any(errors.values()):
        return True

    # Collect all error messages
    all_errors = []
    for category, messages in errors.items():
        all_errors.extend(messages)

    # If only one error, raise it directly
    if len(all_errors) == 1:
        raise Invalid(all_errors[0])

    # Otherwise raise all errors together
    if all_errors:
        raise Invalid('\n'.join(all_errors))

    return True