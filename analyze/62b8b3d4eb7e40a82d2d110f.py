def _should_attempt_c_optimizations():
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    import os
    import sys

    # Check if we are running on PyPy
    is_pypy = 'pypy' in sys.version.lower()

    # Check the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON')

    # If we are on PyPy and PURE_PYTHON is not set, we can use C optimizations
    if is_pypy and pure_python is None:
        return True

    # Otherwise, we should not attempt C optimizations
    return False