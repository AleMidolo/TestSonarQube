def vertex3tuple(vertices):
    """
    获取多边形每个顶点的3个点。  
    这将包括顶点本身以及顶点两侧的两个点。  
    如果下标超出范围，则将索引值视为0。  
    参数：
        vertices：需要转换的顶点列表。
    返回值：
        返回一个列表，其中每个元素是由顶点表示的元组。

    对于多边形的每个顶点，返回3个点。这包括顶点本身以及顶点两侧的两个点。

    假设多边形的顶点为 `A, B, C, D`，  
    函数将返回以下结果：  
    `DAB, ABC, BCD, CDA` -> 返回3个点的元组。
    # A    B    C    D  -> 顶点
    """
    n = len(vertices)
    result = []
    
    for i in range(n):
        left = vertices[i - 1] if i > 0 else vertices[0]
        center = vertices[i]
        right = vertices[i + 1] if i < n - 1 else vertices[-1]
        result.append((left, center, right))
    
    return result