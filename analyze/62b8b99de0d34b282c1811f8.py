def _reset_logging(cls):
    """
    重置日志系统
    """
    import logging
    
    # Remove all existing handlers
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        
    # Reset logging configuration
    logging.shutdown()
    logging.basicConfig(level=logging.INFO,
                       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                       datefmt='%Y-%m-%d %H:%M:%S')