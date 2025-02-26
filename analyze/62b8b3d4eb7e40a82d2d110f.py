def _should_attempt_c_optimizations():
    import os
    import sys

    # Check if we are running on PyPy
    is_pypy = 'pypy' in sys.version.lower()

    # Check the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON')

    # Return True if we are not on PyPy or if PURE_PYTHON is not set
    return not is_pypy or pure_python is None