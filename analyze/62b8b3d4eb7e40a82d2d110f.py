def _should_attempt_c_optimizations():
    import os
    from platform import python_implementation

    is_pypy = python_implementation() == 'PyPy'
    pure_python = os.getenv('PURE_PYTHON', '0') == '1'

    return is_pypy and not pure_python