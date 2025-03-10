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
    import sys

    # 获取异常的堆栈信息
    exc_type, exc_value, exc_traceback = sys.exc_info()
    stack = traceback.extract_tb(exc_traceback)

    # 限制堆栈层级
    if len(stack) > max_level:
        stack = stack[:max_level]

    # 格式化堆栈信息
    stack_str = []
    for frame in stack:
        file_path = frame.filename
        # 限制路径层级
        if max_path_level > 0:
            parts = file_path.split('/')
            if len(parts) > max_path_level:
                file_path = '/'.join(parts[-max_path_level:])
        stack_str.append(f"File \"{file_path}\", line {frame.lineno}, in {frame.name}\n  {frame.line}")

    # 格式化异常信息
    exception_str = f"{exc_type.__name__}: {exc_value}\n"
    exception_str += "\n".join(stack_str)

    return exception_str