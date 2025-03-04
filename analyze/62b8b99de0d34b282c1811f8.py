def _reset_logging(cls):  
    """
    Reimposta
    """
    # Assuming we want to reset the logging configuration
    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=logging.NOTSET)