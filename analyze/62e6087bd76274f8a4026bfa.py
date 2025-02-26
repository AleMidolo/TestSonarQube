def pop_u16(self):
    """
    在 `self.data` 中移除最后两个元素并返回
    移除数据中的最后两个字节，并将它们以大端序的16位无符号整数返回。
    """
    if len(self.data) < 2:
        raise IndexError("Not enough data to pop two bytes.")
    
    # 移除最后两个字节
    byte1 = self.data.pop()
    byte2 = self.data.pop()
    
    # 将字节转换为大端序的16位无符号整数
    return (byte2 << 8) | byte1