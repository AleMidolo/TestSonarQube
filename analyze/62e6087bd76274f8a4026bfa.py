def pop_u16(self):
    """
    在 `self.data` 中移除最后两个元素并返回
    移除数据中的最后两个字节，并将它们以大端序的16位无符号整数返回。
    """
    # 从末尾取出两个字节
    b1 = self.data.pop()
    b2 = self.data.pop()
    
    # 按大端序组合成16位无符号整数
    # b2为高字节,b1为低字节
    return (b2 << 8) | b1