def _reset_logging(cls):
    """
    Reset logging configuration to default state
    """
    import logging
    
    # Remove all existing handlers
    root = logging.getLogger()
    for handler in root.handlers[:]:
        root.removeHandler(handler)
        
    # Reset logger level to default
    root.setLevel(logging.WARNING)
    
    # Add default stream handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)