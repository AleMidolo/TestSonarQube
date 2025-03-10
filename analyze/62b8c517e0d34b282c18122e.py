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
    if exc_traceback is None:
        exc_traceback = e.__traceback__

    # Format the exception
    tb_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
    tb_str = "".join(tb_list)

    # Limit the call stack level
    if max_level is not None:
        tb_lines = tb_str.splitlines()
        if len(tb_lines) > max_level:
            tb_lines = tb_lines[:max_level]
            tb_lines.append("... (call stack truncated)")
        tb_str = "\n".join(tb_lines)

    # Limit the path level
    if max_path_level is not None:
        tb_lines = tb_str.splitlines()
        for i, line in enumerate(tb_lines):
            if "File" in line and "line" in line:
                parts = line.split(", ")
                if len(parts) > 1:
                    path = parts[0].split("File ")[1]
                    path_parts = path.split("/")
                    if len(path_parts) > max_path_level:
                        path_parts = path_parts[-max_path_level:]
                        path = "/".join(path_parts)
                        tb_lines[i] = f"File {path}, {parts[1]}"
        tb_str = "\n".join(tb_lines)

    return tb_str