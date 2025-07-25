def _reset_logging(cls):
    """
    Reset the logging configuration to its default state.
    """
    import logging
    logging.root.handlers = []
    logging.root.setLevel(logging.WARNING)