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
    import os

    # 获取异常的堆栈信息
    stack = traceback.extract_tb(e.__traceback__)
    stack_str = []

    # 限制堆栈层级
    stack = stack[:max_level]

    for frame in stack:
        # 限制路径层级
        path = frame.filename
        path_parts = path.split(os.sep)
        if len(path_parts) > max_path_level:
            path = os.sep.join(path_parts[-max_path_level:])
        
        # 格式化每一帧的堆栈信息
        stack_str.append(f"File \"{path}\", line {frame.lineno}, in {frame.name}\n    {frame.line}")

    # 将堆栈信息拼接成字符串
    stack_str = "\n".join(stack_str)
    
    # 获取异常类型和消息
    exception_type = type(e).__name__
    exception_msg = str(e)

    # 拼接完整的异常信息
    result = f"{exception_type}: {exception_msg}\n{stack_str}"
    
    return result