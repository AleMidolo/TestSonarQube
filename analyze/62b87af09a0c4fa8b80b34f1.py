def fill(self, coord, weight=1):
    """
    根据给定的 *weight* 在 *coord* 处填充直方图。
    
    超出直方图边界的坐标将被忽略。
    """
    # 检查坐标是否为序列类型
    if not hasattr(coord, '__iter__'):
        raise TypeError("coord must be a sequence")
        
    # 检查坐标维度是否与直方图维度匹配
    if len(coord) != self.ndim:
        raise ValueError(f"coord must have {self.ndim} dimensions")
        
    # 检查坐标是否在直方图边界内
    for i, x in enumerate(coord):
        if x < 0 or x >= self.shape[i]:
            return  # 忽略超出边界的坐标
            
    # 将坐标转换为整数索引
    idx = tuple(int(x) for x in coord)
    
    # 在指定位置增加权重
    self.data[idx] += weight