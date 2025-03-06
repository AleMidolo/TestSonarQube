def _reset_logging(cls):
    """
    Reimposta la configurazione del logging al suo stato iniziale.
    """
    import logging
    logging.root.handlers = []
    logging.root.setLevel(logging.WARNING)