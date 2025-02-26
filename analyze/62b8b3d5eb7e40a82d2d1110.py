def _c_optimizations_available():
    """
    Restituisce il modulo di ottimizzazione C, se disponibile, altrimenti un valore falso.

    Se le ottimizzazioni sono richieste ma non disponibili, viene sollevata un'eccezione `ImportError`.

    Questo non specifica se le ottimizzazioni debbano essere utilizzate o meno.
    """
    try:
        import some_c_optimization_module  # Sostituisci con il nome reale del modulo
        return some_c_optimization_module
    except ImportError:
        raise ImportError("Le ottimizzazioni C sono richieste ma non disponibili.")
    return False