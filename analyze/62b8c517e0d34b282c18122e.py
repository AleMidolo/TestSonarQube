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
    tb_list = traceback.format_exception(type(e), e, e.__traceback__)

    # 限制堆栈层级
    if len(tb_list) > max_level:
        tb_list = tb_list[:max_level]
        tb_list.append(f"... (truncated to {max_level} levels)")

    # 限制路径层级
    for i in range(len(tb_list)):
        parts = tb_list[i].split(os.sep)
        if len(parts) > max_path_level:
            parts = parts[-max_path_level:]
            tb_list[i] = os.sep.join(parts)

    # 将堆栈信息拼接成字符串
    return ''.join(tb_list)