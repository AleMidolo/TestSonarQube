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
    if tb is None:
        tb = e.__traceback__

    # Limit the traceback to max_level
    if tb is not None:
        tb = traceback.extract_tb(tb, limit=max_level)

    # Format the exception message
    exception_message = f"{type(e).__name__}: {str(e)}"

    # Format the traceback
    if tb is not None:
        formatted_traceback = []
        for frame in tb:
            # Limit the path level
            file_path = frame.filename
            if max_path_level > 0:
                file_path = "/".join(file_path.split("/")[-max_path_level:])
            formatted_traceback.append(f"  File \"{file_path}\", line {frame.lineno}, in {frame.name}")
            if frame.line:
                formatted_traceback.append(f"    {frame.line.strip()}")

        formatted_traceback = "\n".join(formatted_traceback)
        exception_message = f"{exception_message}\n{formatted_traceback}"

    return exception_message