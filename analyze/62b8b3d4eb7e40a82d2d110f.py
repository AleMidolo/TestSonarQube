def _should_attempt_c_optimizations():
    """
    Restituisce un valore vero se dovremmo tentare di utilizzare le ottimizzazioni in C.

    Questo tiene conto del fatto che stiamo utilizzando PyPy e del valore della variabile di ambiente  
    ``PURE_PYTHON``, come definito in `_use_c_impl`.
    """
    import os
    import platform

    # Check if running on PyPy
    is_pypy = platform.python_implementation() == 'PyPy'

    # Check PURE_PYTHON environment variable
    pure_python = os.environ.get('PURE_PYTHON', '').lower()
    use_pure_python = pure_python in ('1', 'true', 'yes', 'on')

    # Return True only if not PyPy and not using pure Python
    return not (is_pypy or use_pure_python)