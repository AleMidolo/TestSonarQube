import logging

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
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # 创建一个文件处理器，用于将日志写入文件
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    # 创建一个控制台处理器，用于将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    # 创建一个格式化器并将其添加到处理器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger