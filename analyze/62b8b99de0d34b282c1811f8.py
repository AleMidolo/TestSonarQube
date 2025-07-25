def _reset_logging(cls):
    """
    Reimposta
    """
    # Reset logging configuration to default state
    import logging
    
    # Remove all existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
        
    # Reset logging level to default WARNING
    logging.root.setLevel(logging.WARNING)
    
    # Reset logging configuration
    logging.basicConfig()