def _reset_logging(cls):
    """
    重置日志系统
    """
    import logging
    logging.shutdown()
    logging.root.handlers.clear()
    logging.root.setLevel(logging.NOTSET)