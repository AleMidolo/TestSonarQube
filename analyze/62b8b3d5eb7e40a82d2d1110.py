def _c_optimizations_available():
    """
    Restituisce il modulo di ottimizzazione C, se disponibile, altrimenti un valore falso.

    Se le ottimizzazioni sono richieste ma non disponibili, viene sollevata un'eccezione `ImportError`.

    Questo non specifica se le ottimizzazioni debbano essere utilizzate o meno.
    """
    try:
        import c_optimizations  # Supponendo che il modulo si chiami c_optimizations
        return c_optimizations
    except ImportError:
        raise ImportError("Le ottimizzazioni C sono richieste ma non disponibili.")