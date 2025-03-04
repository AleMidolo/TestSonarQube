def _should_attempt_c_optimizations():
    import os
    import platform

    # Check if running on PyPy
    is_pypy = platform.python_implementation() == 'PyPy'
    
    # Get PURE_PYTHON environment variable, defaulting to None if not set
    pure_python = os.environ.get('PURE_PYTHON')
    
    # Return True only if:
    # 1. Not running on PyPy
    # 2. PURE_PYTHON env var is not set to any truthy value
    return not is_pypy and not pure_python