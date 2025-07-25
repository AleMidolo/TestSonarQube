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

    # 获取异常信息
    exc_type, exc_value, exc_traceback = sys.exc_info()
    
    # 格式化异常信息
    formatted_exception = traceback.format_exception(exc_type, exc_value, exc_traceback, limit=max_level)
    
    # 限制路径层级
    formatted_exception = [line for line in formatted_exception if line.count('/') <= max_path_level]
    
    # 将列表转换为字符串
    exception_str = ''.join(formatted_exception)
    
    return exception_str