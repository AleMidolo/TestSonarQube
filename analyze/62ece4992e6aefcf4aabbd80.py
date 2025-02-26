def remove_ending_os_sep(input_list):
    """
    如果输入列表为 None，则返回 []

    遍历字符串列表并移除末尾的操作系统分隔符。

    函数会检测每个字符的长度是否大于 1，并且最后一个字符是否为路径分隔符。

    返回值：
    移除末尾操作系统分隔符后的列表。

    遍历字符串列表并移除末尾的操作系统分隔符字符。

    函数会检测每个字符的长度是否大于 1，并且最后一个字符是否为路径分隔符。如果是，则移除路径分隔符。

    参数：
      `input_list`: 字符串列表

    返回值：
      处理后的字符串列表

    异常：
      `TypeError`
    """
    import os

    if input_list is None:
        return []

    if not isinstance(input_list, list):
        raise TypeError("input_list must be a list")

    result = []
    for item in input_list:
        if isinstance(item, str) and len(item) > 1:
            if item[-1] == os.sep:
                result.append(item[:-1])
            else:
                result.append(item)
        else:
            result.append(item)

    return result