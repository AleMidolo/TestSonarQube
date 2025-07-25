from zope.interface import providedBy, verify
from zope.interface.exceptions import Invalid

def verifyObject(iface, candidate, tentative=False):
    """
    Verify that the candidate correctly provides the interface.

    This includes:

    - Ensuring that the candidate claims to provide the interface,
      using ``iface.providedBy`` (unless *tentative* is `True`,
      in which case this step is skipped). This means that the candidate's class
      declares that it implements the interface with `implements <zope.interface.implementer>`,
      or the candidate itself declares that it provides the interface with
      `provides <zope.interface.provider>`.

    - Ensuring that the candidate defines all required methods.

    - Ensuring that the method signatures are correct (as far as possible).

    - Ensuring that the candidate defines all required attributes.

    :return bool: Returns a truth value if all checks pass.
    :raises zope.interface.Invalid: If any of the above conditions are not met.

    .. versionchanged:: 5.0
        If multiple methods or attributes are invalid, all errors are collected and reported.
        Previously, only the first error was reported. In a special case, if only one error exists,
        it is raised alone as before.
    """
    errors = []

    # Step 1: Verify that the candidate claims to provide the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(f"The candidate does not claim to provide the interface {iface}.")

    # Step 2: Verify that the candidate defines all required methods
    try:
        verify.verifyClass(iface, candidate.__class__)
    except Invalid as e:
        errors.append(str(e))

    # Step 3: Verify that the candidate defines all required attributes
    try:
        verify.verifyObject(iface, candidate)
    except Invalid as e:
        errors.append(str(e))

    # If there are any errors, raise them
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True