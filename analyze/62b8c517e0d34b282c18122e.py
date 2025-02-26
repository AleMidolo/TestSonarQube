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
            return f"{exc.__class__.__name__}: {str(exc)}\n[...]\n"
        
        tb = traceback.extract_tb(exc.__traceback__)
        formatted_tb = []
        for frame in tb[:max_path_level]:
            formatted_tb.append(f"File \"{frame.filename}\", line {frame.lineno}, in {frame.name}")
        
        return f"{exc.__class__.__name__}: {str(exc)}\n" + "\n".join(formatted_tb) + "\n"

    return format_exception(e, 0, 0)