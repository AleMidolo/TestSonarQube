def _reset_logging(cls):
    """
    Reset logging configuration to default settings.
    """
    import logging
    logging.root.handlers = []
    logging.root.setLevel(logging.WARNING)
    logging.basicConfig(level=logging.WARNING)