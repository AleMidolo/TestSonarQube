import os

def _should_attempt_c_optimizations():
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    # Check if we're running on PyPy
    is_pypy = hasattr(sys, 'pypy_version_info')
    
    # Check the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON', '').lower() in ('1', 'true', 'yes')
    
    # Attempt C optimizations if not on PyPy and PURE_PYTHON is not set to True
    return not is_pypy and not pure_python