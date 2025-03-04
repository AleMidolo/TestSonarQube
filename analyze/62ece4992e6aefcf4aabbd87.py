def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    General purpose application logger. Useful mainly for debugging
    """
    import logging

    # Create logger
    logger = logging.getLogger(name)
    
    # Set logging level
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Create handlers
    file_handler = logging.FileHandler(logfile)
    console_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger