def extostr(cls, e, max_level=30, max_path_level=5):
    """
    将异常格式化为字符串
    格式化异常信息。

    :param e: 任意异常实例。
    :type e: Exception
    :param max_level: 最大调用堆栈层级（默认值为30）
    :type max_level: int
    :param max_path_level: 最大路径层级（默认值为5）
    :type max_path_level: int
    :return: 可读的异常字符串
    :rtype: str
    """
    import traceback

    def format_exception(exc, level, path_level):
        if level > max_level:
            return f"{exc.__class__.__name__}: {str(exc)}\n"

        tb_lines = traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        formatted_tb = ''.join(tb_lines)

        if path_level > max_path_level:
            return f"{exc.__class__.__name__}: {str(exc)}\n"

        return formatted_tb

    return format_exception(e, 0, 0)