def fill(self, coord, weight=1):
    """
    根据给定的 *weight* 在 *coord* 处填充直方图。
    
    超出直方图边界的坐标将被忽略。
    """
    # 检查坐标是否为有效的元组或列表
    if not isinstance(coord, (tuple, list)):
        return
        
    # 检查坐标维度是否与直方图维度匹配
    if len(coord) != len(self.shape):
        return
        
    # 检查坐标是否在直方图边界内
    for i, c in enumerate(coord):
        if c < 0 or c >= self.shape[i]:
            return
            
    # 将坐标转换为整数元组
    coord = tuple(int(c) for c in coord)
    
    # 在指定位置增加权重
    self.data[coord] += weight