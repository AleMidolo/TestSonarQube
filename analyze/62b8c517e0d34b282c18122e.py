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

    # Get the exception type and message
    exc_type = type(e).__name__
    exc_msg = str(e)

    # Get the traceback
    tb_list = traceback.format_tb(sys.exc_info()[2])

    # Limit the traceback to max_level
    if len(tb_list) > max_level:
        tb_list = tb_list[:max_level]

    # Format the traceback
    formatted_tb = []
    for i, tb in enumerate(tb_list):
        if i >= max_path_level:
            break
        formatted_tb.append(tb.strip())

    # Combine the exception type, message, and traceback
    result = f"{exc_type}: {exc_msg}\n"
    result += "\n".join(formatted_tb)

    return result