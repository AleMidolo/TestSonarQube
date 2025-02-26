def extostr(cls, e, max_level=30, max_path_level=5):
    """
    Format an exception.
    :param e: Any exception instance.
    :type e: Exception
    :param max_level: Maximum call stack level (default 30)
    :type max_level: int
    :param max_path_level: Maximum path level (default 5)
    :type max_path_level: int
    :return: The exception readable string
    :rtype: str
    """
    import traceback

    def format_traceback(tb, level):
        if level > max_level or tb is None:
            return ""
        return format_traceback(tb.tb_next, level + 1) + f"File \"{tb.tb_frame.f_code.co_filename}\", line {tb.tb_lineno}, in {tb.tb_frame.f_code.co_name}\n"

    exception_message = f"{type(e).__name__}: {str(e)}\n"
    tb = e.__traceback__
    formatted_traceback = format_traceback(tb, 0)

    return exception_message + formatted_traceback