def pop_u16(self):
    """
    在 `self.data` 中移除最后两个元素并返回
    移除数据中的最后两个字节，并将它们以大端序的16位无符号整数返回。
    """
    if len(self.data) < 2:
        raise ValueError("Not enough data to pop a 16-bit unsigned integer.")
    
    # 获取最后两个字节
    byte1 = self.data.pop()
    byte2 = self.data.pop()
    
    # 以大端序组合成16位无符号整数
    u16_value = (byte2 << 8) | byte1
    
    return u16_value