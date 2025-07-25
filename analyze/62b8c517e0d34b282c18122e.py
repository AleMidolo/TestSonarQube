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
        if level <= 0 or path_level <= 0:
            return "..."  # Limit reached
        tb = traceback.extract_tb(exc.__traceback__)
        formatted_tb = []
        for frame in tb[:max_level]:
            formatted_tb.append(f"File \"{frame.filename}\", line {frame.lineno}, in {frame.name}")
        return "\n".join(formatted_tb)

    exception_message = str(e)
    formatted_traceback = format_exception(e, max_level, max_path_level)
    
    return f"{type(e).__name__}: {exception_message}\nTraceback (most recent call last):\n{formatted_traceback}"