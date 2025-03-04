def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    Logger per applicazioni di uso generale. Utile principalmente per il debugging.
    """
    import logging

    # Create logger
    logger = logging.getLogger(name)
    
    # Set logging level
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Create formatters
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    # Create file handler
    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger