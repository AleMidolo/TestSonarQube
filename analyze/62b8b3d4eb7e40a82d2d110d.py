def _c_optimizations_required():
    """
    Restituisce un valore vero se le ottimizzazioni in C sono richieste.

    Questo utilizza la variabile ``PURE_PYTHON`` come     
    documentato in `_use_c_impl`.
    """
    try:
        # Check if PURE_PYTHON environment variable is set
        import os
        pure_python = os.environ.get('PURE_PYTHON', '0').lower()
        return pure_python not in ('1', 'true', 'yes', 'on')
    except:
        # Default to True if environment check fails
        return True