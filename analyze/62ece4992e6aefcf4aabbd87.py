import logging
import os

def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    General purpose application logger. Useful mainly for debugging
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # Create a file handler
    if not os.path.exists(os.path.dirname(logfile)):
        os.makedirs(os.path.dirname(logfile), exist_ok=True)
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)

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