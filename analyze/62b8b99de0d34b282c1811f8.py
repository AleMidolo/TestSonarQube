def _reset_logging(cls):
    """
    重置日志系统
    """
    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=logging.NOTSET)