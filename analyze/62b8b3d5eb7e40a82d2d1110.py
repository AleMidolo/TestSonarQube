def _c_optimizations_available():
    """
    Devuelve el módulo de optimización en C, si está disponible, de lo contrario, un valor falso.

    Si las optimizaciones son requeridas pero no están disponibles, esto genera una excepción `ImportError`.

    Esto no indica si deben ser utilizadas o no.
    """
    try:
        import c_optimizations  # Suponiendo que el módulo se llama c_optimizations
        return c_optimizations
    except ImportError:
        return False