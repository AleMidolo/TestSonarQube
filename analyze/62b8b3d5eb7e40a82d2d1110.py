def _c_optimizations_available():
    """
    Restituisce il modulo di ottimizzazione C, se disponibile, altrimenti un valore falso.

    Se le ottimizzazioni sono richieste ma non disponibili, viene sollevata un'eccezione `ImportError`.

    Questo non specifica se le ottimizzazioni debbano essere utilizzate o meno.
    """
    try:
        import _c_optimizations
        return _c_optimizations
    except ImportError:
        return False