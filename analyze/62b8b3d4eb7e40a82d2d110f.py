def _should_attempt_c_optimizations():
    import os
    import sys

    # Check if we are running on PyPy
    is_pypy = 'pypy' in sys.version.lower()

    # Check the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON')

    # Determine if we should attempt C optimizations
    if is_pypy:
        return False  # Do not attempt C optimizations on PyPy
    return pure_python is None  # Attempt C optimizations if PURE_PYTHON is not set