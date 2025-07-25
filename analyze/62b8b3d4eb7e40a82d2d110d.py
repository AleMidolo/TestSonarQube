def _c_optimizations_required():
    """
    Restituisce un valore vero se le ottimizzazioni in C sono richieste.

    Questo utilizza la variabile ``PURE_PYTHON`` come     
    documentato in `_use_c_impl`.
    """
    try:
        from os import environ
        pure_python = environ.get('PURE_PYTHON', '').lower()
        return pure_python not in ('1', 'true', 'yes', 'on')
    except ImportError:
        return True