def _should_attempt_c_optimizations():
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    import os
    import sys

    # Check if we are on PyPy
    is_pypy = 'pypy' in sys.version.lower()

    # Check the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON')

    # If we are on PyPy and PURE_PYTHON is not set, we can use C optimizations
    if is_pypy and pure_python is None:
        return True

    # If PURE_PYTHON is set to '1', we should not use C optimizations
    if pure_python == '1':
        return False

    # In all other cases, we can attempt to use C optimizations
    return True