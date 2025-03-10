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
    tb_str = ''.join(tb_list)

    # 限制堆栈层级
    if max_level > 0:
        tb_lines = tb_str.splitlines()
        tb_str = '\n'.join(tb_lines[:max_level])

    # 限制路径层级
    if max_path_level > 0:
        tb_lines = tb_str.splitlines()
        for i in range(len(tb_lines)):
            if 'File "' in tb_lines[i]:
                path = tb_lines[i].split('"')[1]
                parts = path.split(os.sep)
                if len(parts) > max_path_level:
                    parts = parts[-max_path_level:]
                    tb_lines[i] = tb_lines[i].replace(path, os.sep.join(parts))
        tb_str = '\n'.join(tb_lines)

    return tb_str