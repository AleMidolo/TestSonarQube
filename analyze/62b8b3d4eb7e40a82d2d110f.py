def _should_attempt_c_optimizations():
    import os
    import platform

    # Check if running on PyPy
    is_pypy = platform.python_implementation() == 'PyPy'
    
    # Get PURE_PYTHON environment variable, defaulting to None if not set
    pure_python = os.environ.get('PURE_PYTHON')
    
    # Return False if on PyPy or if PURE_PYTHON is set to a true value
    if is_pypy:
        return False
        
    if pure_python:
        # Check various string values that could indicate True
        return not pure_python.lower() in ('1', 'true', 't', 'yes', 'y', 'on')
        
    return True