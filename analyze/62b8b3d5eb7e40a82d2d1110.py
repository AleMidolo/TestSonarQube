def _c_optimizations_available():
    try:
        import some_c_optimization_module  # Sostituisci con il modulo reale
        return some_c_optimization_module
    except ImportError:
        raise ImportError("Le ottimizzazioni C sono richieste ma non disponibili.")