def vertex3tuple(vertices):
    """
    获取多边形每个顶点的3个点。  
    这将包括顶点本身以及顶点两侧的两个点。  
    如果下标超出范围，则将索引值视为0。  
    参数：
        vertices：需要转换的顶点列表。
    返回值：
        返回一个列表，其中每个元素是由顶点表示的元组。
    """
    result = []
    n = len(vertices)
    
    for i in range(n):
        # 获取前一个点的索引
        prev_idx = (i - 1) % n
        # 获取当前点的索引
        curr_idx = i
        # 获取后一个点的索引
        next_idx = (i + 1) % n
        
        # 创建包含3个点的元组
        triple = (vertices[prev_idx], vertices[curr_idx], vertices[next_idx])
        result.append(triple)
        
    return result