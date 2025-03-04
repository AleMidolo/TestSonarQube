def _should_attempt_c_optimizations():
    import os
    import platform

    # Check if running on PyPy
    is_pypy = platform.python_implementation() == 'PyPy'
    
    # Check PURE_PYTHON environment variable
    pure_python = os.environ.get('PURE_PYTHON', '').lower()
    use_pure_python = pure_python in ('1', 'true', 't', 'yes', 'y')

    # Return True only if not PyPy and not using pure Python
    return not (is_pypy or use_pure_python)