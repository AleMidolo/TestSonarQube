def _reset_logging(cls):
    """
    Reimposta la configurazione del logging alla sua configurazione iniziale.
    """
    import logging
    logging.shutdown()
    logging.root.handlers = []
    logging.basicConfig()