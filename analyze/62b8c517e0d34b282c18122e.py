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
    
    # Add the traceback to the message
    exception_message += "".join(limited_tb)
    
    # Limit the path levels in the traceback
    if max_path_level > 0:
        lines = exception_message.splitlines()
        for i in range(len(lines)):
            if "File" in lines[i] and "line" in lines[i]:
                path = lines[i].split(",")[0].split("File ")[1].strip()
                path_parts = path.split("/")
                if len(path_parts) > max_path_level:
                    path_parts = path_parts[-max_path_level:]
                    lines[i] = lines[i].replace(path, ".../" + "/".join(path_parts))
        exception_message = "\n".join(lines)
    
    return exception_message