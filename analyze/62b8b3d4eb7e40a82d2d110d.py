def _c_optimizations_required():
    """
    Devuelve un valor verdadero si se requieren las optimizaciones en C.

    Esto utiliza la variable ``PURE_PYTHON`` como se documenta en `_use_c_impl`.
    """
    try:
        from os import environ
        pure_python = environ.get('PURE_PYTHON', '').lower()
        return pure_python not in ('1', 'true', 't', 'yes', 'y')
    except ImportError:
        return True