def _c_optimizations_required():
    """
    Restituisce un valore vero se le ottimizzazioni in C sono richieste.

    Questo utilizza la variabile ``PURE_PYTHON`` come     
    documentato in `_use_c_impl`.
    """
    return not PURE_PYTHON