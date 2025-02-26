def _reset_logging(cls):
    """
    Reset the logging configuration to its default state.
    """
    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=logging.NOTSET)