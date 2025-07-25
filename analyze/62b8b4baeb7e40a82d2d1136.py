def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors['general'].append(
            f"Class {candidate.__class__.__name__} does not implement interface {iface.__name__}"
        )

    # Check methods
    for name, desc in iface.namesAndDescriptions(1):
        if isinstance(desc, Method):
            # Check if method exists
            if not hasattr(candidate, name):
                errors['methods'].append(
                    f"Method '{name}' not provided by {candidate.__class__.__name__}"
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
                    errors['methods'].append(
                        f"Method '{name}' has incorrect signature. "
                        f"Expected {iface_sig}, got {impl_sig}"
                    )
            except (ValueError, TypeError):
                pass  # Skip signature checking if not possible

        else:  # Attribute
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"Attribute '{name}' not provided by {candidate.__class__.__name__}"
                )

    # If there are any errors, raise them
    if errors:
        all_errors = []
        for category, category_errors in errors.items():
            all_errors.extend(category_errors)
            
        if len(all_errors) == 1:
            raise Invalid(all_errors[0])
        elif all_errors:
            raise Invalid('\n'.join(all_errors))

    return True