def _reset_logging(cls):
    """
    Restablecer la configuración de logging a su estado inicial.
    """
    import logging
    logging.root.handlers = []
    logging.root.setLevel(logging.WARNING)