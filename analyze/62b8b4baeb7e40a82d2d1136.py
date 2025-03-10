from zope.interface import Invalid, providedBy
from zope.interface.verify import verifyObject, verifyClass

def _verify(iface, candidate, tentative=False, vtype=None):
    """
    Verify that the candidate correctly provides the interface.

    This includes:

    - Ensuring that the candidate claims to provide the interface,
      using ``iface.providedBy`` (unless *tentative* is `True`,
      in which case this step is skipped). This means that the candidate's class
      declares that it implements the interface with `implements <zope.interface.implementer>`,
      or the candidate itself declares that it provides the interface
      with `provides <zope.interface.provider>`.

    - Ensuring that the candidate defines all required methods.

    - Ensuring that the methods have the correct signatures
      (as far as possible).

    - Ensuring that the candidate defines all required attributes.

    :return bool: Returns a true value if all checks pass.
    :raises zope.interface.Invalid: If any of the above conditions are not met.

    .. versionchanged:: 5.0
        If multiple methods or attributes are invalid, all errors are collected and reported.
        Previously, only the first error was reported.
        In a special case, if only one error exists, it is raised alone as before.
    """
    errors = []

    # Step 1: Verify that the candidate claims to provide the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(f"{candidate} does not claim to provide {iface}.")

    # Step 2: Verify that the candidate defines all required methods and attributes
    try:
        if vtype == 'object':
            verifyObject(iface, candidate)
        elif vtype == 'class':
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