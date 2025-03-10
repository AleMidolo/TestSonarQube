def size_to_bytes(size: str) -> int:
    """
    将人类可读的文件大小转换为字节。

    参数:
        size: str，一个表示人类可读的文件大小的字符串 (例如: '500K')
    返回值:
        int: 文件大小的字节数

    结果值是一个近似值，因为输入值在大多数情况下是四舍五入的。

    参数:
        size: 一个表示人类可读文件大小的字符串 (例如: '500K')

    返回值:
        文件大小的十进制表示

    示例::

        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000
    """
    size = size.upper()
    if size[-1] == 'K':
        return int(size[:-1]) * 1000
    elif size[-1] == 'M':
        return int(size[:-1]) * 1000 * 1000
    elif size[-1] == 'G':
        return int(size[:-1]) * 1000 * 1000 * 1000
    elif size[-1] == 'T':
        return int(size[:-1]) * 1000 * 1000 * 1000 * 1000
    else:
        return int(size)