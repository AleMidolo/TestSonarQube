def _reset_logging(cls):
    """
    重置日志系统
    """
    import logging
    logging.shutdown()
    logging.root.handlers = []
    logging.root.setLevel(logging.NOTSET)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    for logger in logging.Logger.manager.loggerDict.values():
        if isinstance(logger, logging.Logger):
            logger.handlers = []
            logger.setLevel(logging.NOTSET)
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)