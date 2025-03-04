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

    # Check methods and attributes
    for name, desc in iface.namesAndDescriptions(all=True):
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

            # Check method signature
            try:
                from inspect import signature
                impl_sig = signature(method)
                iface_sig = signature(desc)

                if impl_sig.parameters != iface_sig.parameters:
                    errors['signatures'].append(
                        f"Method '{name}' has incorrect signature: {impl_sig} != {iface_sig}"
                    )
            except ValueError:
                # Can't get signature, skip verification
                pass

        else:
            # Check attributes
            if not hasattr(candidate, name):
                errors['attributes'].append(
                    f"Attribute '{name}' not provided by {candidate.__class__.__name__}"
                )

    # If there are any errors, raise Invalid
    if errors:
        all_errors = []
        for category, category_errors in errors.items():
            all_errors.extend(category_errors)
            
        if len(all_errors) == 1:
            raise Invalid(all_errors[0])
        else:
            raise Invalid("\n".join(all_errors))

    return True