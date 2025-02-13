def _reset_logging(cls):
    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=logging.NOTSET)