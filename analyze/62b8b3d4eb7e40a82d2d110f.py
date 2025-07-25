def _should_attempt_c_optimizations():
    """
    Restituisce un valore vero se dovremmo tentare di utilizzare le ottimizzazioni in C.

    Questo tiene conto del fatto che stiamo utilizzando PyPy e del valore della variabile di ambiente  
    ``PURE_PYTHON``, come definito in `_use_c_impl`.
    """
    import os
    import platform

    # Controlla se stiamo eseguendo su PyPy
    is_pypy = platform.python_implementation() == 'PyPy'

    # Controlla se la variabile di ambiente PURE_PYTHON è impostata
    pure_python = os.getenv('PURE_PYTHON', '').lower() in ('1', 'true', 'yes')

    # Tentiamo le ottimizzazioni in C solo se non siamo su PyPy e PURE_PYTHON non è impostato
    return not is_pypy and not pure_python