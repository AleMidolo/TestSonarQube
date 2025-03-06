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

    # Limit the traceback depth
    if max_level is not None:
        tb = traceback.extract_tb(tb, limit=max_level)

    # Format the exception
    exception_lines = traceback.format_exception(type(e), e, tb)

    # Limit the path depth in the traceback
    if max_path_level is not None:
        for i in range(len(exception_lines)):
            parts = exception_lines[i].split('\n')
            for j in range(len(parts)):
                if 'File "' in parts[j]:
                    path_parts = parts[j].split(', ')
                    if len(path_parts) > 1:
                        path = path_parts[0].split('"')[1]
                        path_segments = path.split('/')
                        if len(path_segments) > max_path_level:
                            shortened_path = '/'.join(path_segments[-max_path_level:])
                            parts[j] = parts[j].replace(path, '.../' + shortened_path)
            exception_lines[i] = '\n'.join(parts)

    return ''.join(exception_lines)