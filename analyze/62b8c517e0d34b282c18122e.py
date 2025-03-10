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
    tb_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
    
    # Limit the traceback to max_level
    if len(tb_list) > max_level:
        tb_list = tb_list[:max_level]
    
    # Join the traceback into a single string
    tb_str = "".join(tb_list)
    
    # Limit the path level in the traceback
    if max_path_level > 0:
        lines = tb_str.splitlines()
        for i in range(len(lines)):
            if "File" in lines[i] and "line" in lines[i]:
                path = lines[i].split(",")[0].split("File ")[1].strip()
                parts = path.split("/")
                if len(parts) > max_path_level:
                    lines[i] = lines[i].replace(path, "/".join(parts[-max_path_level:]))
        tb_str = "\n".join(lines)
    
    return tb_str