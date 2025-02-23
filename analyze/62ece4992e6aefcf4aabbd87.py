import logging
import os

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

    # Create a file handler
    if not os.path.exists(os.path.dirname(logfile)):
        os.makedirs(os.path.dirname(logfile))
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger