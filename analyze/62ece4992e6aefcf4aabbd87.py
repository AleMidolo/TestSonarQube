def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    सामान्य उद्देश्य के लिए एप्लिकेशन लॉगर। मुख्य रूप से डिबगिंग के लिए उपयोगी।
    """
    import logging
    import sys

    # Create logger
    logger = logging.getLogger(name)
    
    # Set logging level
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create formatters
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Create and add file handler
    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Create and add console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger