def is_ipv4(target):
    """
    测试是否为 IPv4 地址。

    返回值：布尔值，如果目标是 IPv4 地址，则返回真，否则返回假。
    """
    # 检查输入是否为字符串
    if not isinstance(target, str):
        return False
        
    # 按点分割字符串
    parts = target.split('.')
    
    # IPv4 地址必须有 4 个部分
    if len(parts) != 4:
        return False
        
    # 检查每个部分
    for part in parts:
        # 检查是否为数字
        if not part.isdigit():
            return False
            
        # 转换为整数
        num = int(part)
        
        # 检查范围是否在 0-255 之间
        if num < 0 or num > 255:
            return False
            
        # 检查是否有前导零
        if len(part) > 1 and part[0] == '0':
            return False
            
    return True