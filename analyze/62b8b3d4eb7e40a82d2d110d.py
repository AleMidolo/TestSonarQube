def _c_optimizations_required():
    """
    Devuelve un valor verdadero si se requieren las optimizaciones en C.

    Esto utiliza la variable ``PURE_PYTHON`` como se documenta en `_use_c_impl`.
    """
    import os
    return not os.getenv('PURE_PYTHON', '').lower() in ('1', 'true', 'yes')