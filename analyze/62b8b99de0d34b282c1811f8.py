def _reset_logging(cls):
    """
    Reset logging configuration to default settings.
    """
    import logging
    logging.basicConfig(level=logging.WARNING)