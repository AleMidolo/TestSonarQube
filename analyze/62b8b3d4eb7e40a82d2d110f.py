def _should_attempt_c_optimizations():
    """
    Restituisce un valore vero se dovremmo tentare di utilizzare le ottimizzazioni in C.

    Questo tiene conto del fatto che stiamo utilizzando PyPy e del valore della variabile di ambiente  
    ``PURE_PYTHON``, come definito in `_use_c_impl`.
    """
    import os
    import sys

    # Controlla se stiamo usando PyPy
    is_pypy = sys.platform.startswith('pypy')

    # Controlla il valore della variabile di ambiente PURE_PYTHON
    pure_python = os.getenv('PURE_PYTHON', '0') == '1'

    # Decidi se tentare ottimizzazioni in C
    return is_pypy and not pure_python