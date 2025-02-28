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
    tb = traceback.format_exception(type(e), e, e.__traceback__)

    # Limit the traceback to max_level
    if len(tb) > max_level:
        tb = tb[:max_level]
        tb.append(f"... (truncated to {max_level} levels)")

    # Limit the path levels in the traceback
    for i in range(len(tb)):
        parts = tb[i].split('\n')
        if len(parts) > 1:
            path_parts = parts[1].split(', ')
            if len(path_parts) > max_path_level:
                path_parts = path_parts[:max_path_level]
                path_parts.append(f"... (truncated to {max_path_level} levels)")
                parts[1] = ', '.join(path_parts)
                tb[i] = '\n'.join(parts)

    # Combine the exception type, message, and traceback
    result = f"{exc_type}: {exc_msg}\n"
    result += ''.join(tb)

    return result