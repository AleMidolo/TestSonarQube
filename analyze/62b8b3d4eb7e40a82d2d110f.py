def _should_attempt_c_optimizations():
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    import os
    import platform

    # Check if running on PyPy
    is_pypy = platform.python_implementation() == 'PyPy'

    # Get PURE_PYTHON environment variable, defaulting to None if not set
    pure_python = os.environ.get('PURE_PYTHON')

    # Return False if on PyPy or if PURE_PYTHON is set to a truthy value
    if is_pypy:
        return False
    if pure_python:
        return not bool(pure_python.lower() in ('1', 'true', 't', 'yes', 'y'))
    
    return True