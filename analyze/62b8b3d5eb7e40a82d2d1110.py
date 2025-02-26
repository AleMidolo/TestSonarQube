def _c_optimizations_available():
    """
    Devuelve el módulo de optimización en C, si está disponible, de lo contrario, un valor falso.

    Si las optimizaciones son requeridas pero no están disponibles, esto genera una excepción `ImportError`.

    Esto no indica si deben ser utilizadas o no.
    """
    try:
        import c_optimizations  # Intentar importar el módulo de optimización en C
        return c_optimizations  # Retornar el módulo si la importación es exitosa
    except ImportError:
        return False  # Retornar falso si el módulo no está disponible