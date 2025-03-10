def _reset_logging(cls):
    """
    रीसेट
    """
    import logging
    logging.shutdown()
    logging.root.handlers = []
    logging.basicConfig()