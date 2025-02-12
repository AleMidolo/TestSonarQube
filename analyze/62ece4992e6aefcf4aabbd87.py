import logging

def build_app_logger(name='app', logfile='app.log', debug=True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    handler = logging.FileHandler(logfile)
    handler.setLevel(logging.DEBUG if debug else logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(handler)
    
    return logger