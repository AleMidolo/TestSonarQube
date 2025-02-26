def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Format an exception.
    :param e: Any exception instance.
    :type e: Exception
    :param max_level: Maximum call stack level (default 30)
    :type max_level: int
    :param max_path_level: Maximum path level (default 5)
    :type max_path_level: int
    :return: The exception readable string
    :rtype: str
    """
    import traceback

    def format_exception(exc, level, path_level):
        if level > max_level:
            return f"{exc.__class__.__name__}: {exc} (truncated)"
        
        tb_lines = traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        formatted_tb = ''.join(tb_lines)

        if path_level > max_path_level:
            return f"{exc.__class__.__name__}: {exc} (path truncated)"
        
        return formatted_tb

    return format_exception(e, 0, 0)