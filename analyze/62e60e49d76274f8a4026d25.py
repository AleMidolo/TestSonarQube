def unit_of_work(metadata=None, timeout=None):
    """
    Questa funzione è un decorator per funzioni di transazione che consente un controllo aggiuntivo su come viene eseguita la transazione.

    Ad esempio, è possibile applicare un timeout::