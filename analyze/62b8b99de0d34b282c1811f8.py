def _reset_logging(cls):
    """
    Reset the logging configuration to its default state.
    """
    import logging
    logging.shutdown()
    logging.root.handlers = []
    logging.basicConfig()