def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Format an exception.
    :param e: Any exception instance.
    :type e: Exception
    :param max_level: Maximum call stack level (default 30)
    :type max_level: int
    :param max_path_level: Maximum path level (default 5)
    :type max_path_level: int
    :return The exception readable string
    :rtype str
    """
    import traceback
    import sys

    # Get the exception traceback
    exc_type, exc_value, exc_traceback = sys.exc_info()
    
    # Format the exception traceback
    formatted_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback, limit=max_level)
    
    # Join the formatted traceback into a single string
    traceback_str = "".join(formatted_traceback)
    
    # Split the traceback string into lines
    traceback_lines = traceback_str.splitlines()
    
    # Limit the number of path levels in each line
    limited_traceback_lines = []
    for line in traceback_lines:
        parts = line.split("\\")
        if len(parts) > max_path_level:
            line = "\\".join(parts[-max_path_level:])
        limited_traceback_lines.append(line)
    
    # Join the limited traceback lines into a single string
    limited_traceback_str = "\n".join(limited_traceback_lines)
    
    return limited_traceback_str