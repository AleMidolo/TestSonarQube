def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    通用应用程序日志记录器。主要用于调试。

    参数:
      name: 日志记录器的名称
      logfile: 需要保存的日志文件
      debug: 是否需要调试

    返回值:
      返回一个实例化的日志记录器对象
    """
    import logging
    import sys

    # 创建logger对象
    logger = logging.getLogger(name)
    
    # 设置日志级别
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # 创建格式化器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 创建文件处理器
    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 创建控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger