def _reset_logging(cls):
    """
    Restablecer la configuración de logging a su estado inicial.
    """
    import logging
    logging.shutdown()
    logging.root.handlers = []
    logging.basicConfig()