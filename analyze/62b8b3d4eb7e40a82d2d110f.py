def _should_attempt_c_optimizations():
    import os
    import sys

    # Check if we are running on PyPy
    is_pypy = 'pypy' in sys.version.lower()

    # Check the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON')

    # If we are on PyPy, we should attempt C optimizations unless PURE_PYTHON is set
    if is_pypy:
        return pure_python is None

    # If we are not on PyPy, we can attempt C optimizations
    return True