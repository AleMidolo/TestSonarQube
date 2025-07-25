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
    tb = sys.exc_info()[2]
    
    # Limit the traceback to max_level
    limited_tb = traceback.format_tb(tb, limit=max_level)
    
    # Format the exception message
    exception_message = f"{type(e).__name__}: {str(e)}\n"
    
    # Format the traceback
    traceback_str = "".join(limited_tb)
    
    # Limit the path levels in the traceback
    if max_path_level > 0:
        traceback_lines = traceback_str.splitlines()
        for i in range(len(traceback_lines)):
            parts = traceback_lines[i].split(", ")
            if len(parts) > 1:
                file_path = parts[0].split('"')[1]
                path_parts = file_path.split('/')
                if len(path_parts) > max_path_level:
                    shortened_path = '/'.join(path_parts[-max_path_level:])
                    traceback_lines[i] = traceback_lines[i].replace(file_path, f".../{shortened_path}")
        traceback_str = "\n".join(traceback_lines)
    
    # Combine the exception message and traceback
    formatted_exception = exception_message + traceback_str
    
    return formatted_exception