def is_valid(self):
    """
    判断IP地址是否有效，即IP地址是否由四个十进制数字组成，并且用'.'分隔。每个数字大于等于0且小于等于255。
    :return: bool
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.is_valid()
    True
    """
    try:
        # 按'.'分割IP地址
        parts = self.ip.split('.')
        
        # 检查是否恰好有4个部分
        if len(parts) != 4:
            return False
        
        # 检查每个部分
        for part in parts:
            # 检查是否为空
            if not part:
                return False
            
            # 检查是否有前导零（除了"0"本身）
            if len(part) > 1 and part[0] == '0':
                return False
            
            # 检查是否全为数字
            if not part.isdigit():
                return False
            
            # 转换为整数并检查范围
            num = int(part)
            if num < 0 or num > 255:
                return False
        
        return True
    except:
        return False