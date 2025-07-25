def fill(self, coord, weight=1):
    """
    根据给定的 *weight* 在 *coord* 处填充直方图。
    
    超出直方图边界的坐标将被忽略。
    """
    # 检查坐标是否为可迭代对象
    if not hasattr(coord, '__iter__'):
        raise TypeError("coord must be iterable")
        
    # 检查坐标维度是否与直方图维度匹配
    if len(coord) != len(self.shape):
        raise ValueError(f"coord dimension {len(coord)} does not match histogram dimension {len(self.shape)}")
        
    # 检查坐标是否在直方图边界内
    for i, c in enumerate(coord):
        if c < 0 or c >= self.shape[i]:
            return  # 忽略超出边界的坐标
            
    # 将坐标转换为整数元组
    idx = tuple(int(c) for c in coord)
    
    # 在指定位置增加权重
    self.data[idx] += weight