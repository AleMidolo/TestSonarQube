def _reset_logging(cls):
    """
    重置日志系统
    """
    import logging
    logging.shutdown()
    logging.root.handlers.clear()
    logging.basicConfig(level=logging.INFO)