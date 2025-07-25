from zope.interface import Invalid, providedBy
from zope.interface.verify import verifyObject, verifyClass

def _verify(iface, candidate, tentative=False, vtype=None):
    """
    Verify that the candidate correctly provides the interface.

    This includes:
    - Ensuring the candidate claims to provide the interface using `iface.providedBy`
      (unless tentative is True, in which case this step is skipped).
    - Ensuring the candidate defines all required methods.
    - Ensuring the methods have the correct signatures (as far as possible).
    - Ensuring the candidate defines all required attributes.

    :return bool: Returns a true value if all checks pass.
    :raises zope.interface.Invalid: If any of the above conditions are not met.
    """
    errors = []

    # Step 1: Verify that the candidate claims to provide the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(f"{candidate} does not claim to provide {iface}.")

    # Step 2: Verify that the candidate defines all required methods and attributes
    try:
        if vtype == 'class':
            verifyClass(iface, candidate)
        else:
            verifyObject(iface, candidate)
    except Invalid as e:
        errors.append(str(e))

    # Step 3: If there are any errors, raise them
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True