def _reset_logging(cls):
    """
    Reset the logging configuration for the class.
    This method will clear any existing logging handlers and reset the logging level to the default.
    """
    for handler in cls.logger.handlers[:]:
        cls.logger.removeHandler(handler)
    cls.logger.setLevel(cls.default_logging_level)