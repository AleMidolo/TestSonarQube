from zope.interface import providedBy, verify
from zope.interface.exceptions import Invalid
from inspect import signature

def verifyObject(iface, candidate, tentative=False):
    """
    Verify that the candidate correctly provides the given interface.

    This includes:
    - Ensuring that the candidate claims to provide the interface using `iface.providedBy`
      (unless *tentative* is `True`, in which case this step is skipped).
    - Ensuring that the candidate defines all required methods.
    - Ensuring that the method signatures are correct (as far as possible).
    - Ensuring that the candidate defines all required attributes.

    :return bool: Returns True if all checks pass.
    :raises zope.interface.Invalid: If any of the above conditions are not met.
    """
    errors = []

    # Step 1: Verify that the candidate claims to provide the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(f"{candidate} does not claim to provide {iface}.")

    # Step 2: Verify that all required methods are defined
    for method_name in iface.names():
        if not hasattr(candidate, method_name):
            errors.append(f"Method '{method_name}' is not defined in {candidate}.")
        else:
            # Step 3: Verify method signatures (if possible)
            try:
                candidate_method = getattr(candidate, method_name)
                iface_method = getattr(iface, method_name)
                candidate_sig = signature(candidate_method)
                iface_sig = signature(iface_method)
                if candidate_sig != iface_sig:
                    errors.append(f"Signature mismatch for method '{method_name}'. Expected {iface_sig}, got {candidate_sig}.")
            except (AttributeError, ValueError):
                # Skip signature verification if not possible
                pass

    # Step 4: Verify that all required attributes are defined
    for attr_name in iface.names(all=True):
        if not hasattr(candidate, attr_name):
            errors.append(f"Attribute '{attr_name}' is not defined in {candidate}.")

    # If there are any errors, raise an Invalid exception with all errors
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True