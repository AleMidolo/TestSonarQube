def _verify(iface, candidate, tentative=False, vtype=None):
    from zope.interface.exceptions import Invalid
    from zope.interface.interface import Method
    from collections import defaultdict

    errors = defaultdict(list)

    # Check if candidate claims to provide interface
    if not tentative and not iface.providedBy(candidate):
        errors['provide'].append(
            f"{candidate!r} does not provide interface {iface!r}"
        )

    # Check methods
    for name, desc in iface.namesAndDescriptions(all=True):
        if not isinstance(desc, Method):
            # Skip non-method attributes for now
            continue
            
        # Check if method exists
        try:
            meth = getattr(candidate, name)
        except AttributeError:
            errors['methods'].append(
                f"The {name!r} method was not provided"
            )
            continue

        # Verify method signature if possible
        if hasattr(desc, 'getSignatureInfo'):
            sig_info = desc.getSignatureInfo()
            try:
                candidate_sig = desc.getSignatureInfo(meth)
                
                # Compare signatures
                if sig_info['positional'] != candidate_sig['positional'] or \
                   sig_info['required'] != candidate_sig['required'] or \
                   sig_info['optional'] != candidate_sig['optional'] or \
                   sig_info['varargs'] != candidate_sig['varargs'] or \
                   sig_info['kwargs'] != candidate_sig['kwargs']:
                    errors['signatures'].append(
                        f"The {name!r} method has incorrect signature"
                    )
            except (TypeError, ValueError):
                errors['signatures'].append(
                    f"Could not verify signature of {name!r} method"
                )

    # Check attributes
    for name, desc in iface.namesAndDescriptions(all=True):
        if isinstance(desc, Method):
            continue
            
        if not hasattr(candidate, name):
            errors['attributes'].append(
                f"The {name!r} attribute was not provided" 
            )

    # If we have errors, raise them
    if errors:
        if sum(len(v) for v in errors.values()) == 1:
            # Special case: single error
            msg = next(err for errs in errors.values() for err in errs)
            raise Invalid(msg)
        
        # Multiple errors
        msgs = []
        for category, errs in errors.items():
            if errs:
                msgs.extend(errs)
        raise Invalid('\n'.join(msgs))

    return True