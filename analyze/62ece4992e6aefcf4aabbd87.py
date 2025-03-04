def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    "Logger" de aplicaciones de propósito general. Útil principalmente para depuración.

    Args:
        name: El nombre del logger.
        logfile: El archivo de registro donde se guardarán los logs.
        debug: Indica si es necesario habilitar la depuración.

    Returns:
        Devuelve un objeto de registrador (logger) instanciado.
    """
    import logging

    # Create logger
    logger = logging.getLogger(name)
    
    # Set logging level based on debug parameter
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add formatter to handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger