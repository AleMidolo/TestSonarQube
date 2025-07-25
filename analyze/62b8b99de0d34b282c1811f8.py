def _reset_logging(cls):
    """
    重置日志系统
    """
    import logging
    
    # 移除所有现有的handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
        
    # 重置logging配置
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )