def size_to_bytes(size: str) -> int:
    """
    将人类可读的文件大小转换为字节。

    参数:
        size: str，一个表示人类可读的文件大小的字符串 (例如: '500K')
    返回值:
        int: 文件大小的字节数
    """
    units = {
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
        'P': 1000000000000000,
        'E': 1000000000000000000,
        'KB': 1000,
        'MB': 1000000,
        'GB': 1000000000,
        'TB': 1000000000000,
        'PB': 1000000000000000,
        'EB': 1000000000000000000
    }

    size = size.strip().upper()
    
    # 如果只有数字,直接返回整数值
    if size.isdigit():
        return int(size)
        
    # 提取数字和单位
    number = ''
    unit = ''
    for char in size:
        if char.isdigit() or char == '.':
            number += char
        else:
            unit += char
            
    # 如果没有找到有效单位,返回原始数字
    if unit not in units:
        return int(float(number))
        
    # 计算字节数
    return int(float(number) * units[unit])