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
    size = size.strip().upper()
    multipliers = {
        'B': 1,
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
    }
    
    if size[-1] in multipliers:
        number = float(size[:-1])
        unit = size[-1]
    else:
        number = float(size)
        unit = 'B'
    
    return int(number * multipliers[unit])