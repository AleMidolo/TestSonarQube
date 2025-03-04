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

    # 获取异常的堆栈跟踪信息
    tb = traceback.extract_tb(e.__traceback__)
    
    # 格式化异常信息
    error_msg = f"{e.__class__.__name__}: {str(e)}\n"
    
    # 添加堆栈跟踪信息
    for i, frame in enumerate(tb):
        if i >= max_level:
            break
            
        filename = frame.filename
        # 处理文件路径,只保留最后max_path_level层
        path_parts = filename.split(os.sep)
        if len(path_parts) > max_path_level:
            filename = os.sep.join(path_parts[-max_path_level:])
            
        line = frame.lineno
        func = frame.name
        text = frame.line
        
        error_msg += f"  File \"{filename}\", line {line}, in {func}\n"
        if text:
            error_msg += f"    {text}\n"
            
    return error_msg