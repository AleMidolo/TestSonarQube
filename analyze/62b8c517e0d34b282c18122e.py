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
    tb = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)

    # Limit the traceback to max_level
    if len(tb) > max_level:
        tb = tb[:max_level] + ["... (truncated due to max_level)\n"]

    # Join the traceback into a single string
    tb_str = "".join(tb)

    # Limit the path level in the traceback
    if max_path_level > 0:
        lines = tb_str.splitlines()
        for i in range(len(lines)):
            if "File" in lines[i]:
                parts = lines[i].split(",")
                if len(parts) > 1:
                    path = parts[0].split("File ")[1].strip()
                    path_parts = path.split("/")
                    if len(path_parts) > max_path_level:
                        path = "/".join(path_parts[-max_path_level:])
                        lines[i] = f"File {path}, {parts[1].strip()}"
        tb_str = "\n".join(lines)

    # Combine the exception type, message, and traceback
    result = f"{exc_type}: {exc_msg}\n{tb_str}"

    return result