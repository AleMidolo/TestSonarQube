def _reset_logging(cls):
    """
    重置日志系统
    """
    import logging
    
    # 移除所有现有的handlers
    root = logging.getLogger()
    for handler in root.handlers[:]:
        root.removeHandler(handler)
        
    # 重置日志级别为默认值
    root.setLevel(logging.WARNING)
    
    # 重置日志格式为默认值
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # 添加新的控制台handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)