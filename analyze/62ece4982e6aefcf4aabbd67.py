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
        # Get previous vertex (wrap around to end if at start)
        prev = vertices[i-1] if i > 0 else vertices[n-1]
        
        # Current vertex
        curr = vertices[i]
        
        # Get next vertex (wrap around to start if at end) 
        next = vertices[(i+1) % n]
        
        # Add tuple of 3 consecutive vertices
        result.append((prev, curr, next))
        
    return result