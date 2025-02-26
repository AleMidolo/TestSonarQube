def integral(bins, edges):
    """
    计算整体图形的面积
    计算积分（直方图的缩放比例）。

    *`bins`* 包含数值，*`edges`* 构成积分的网格。  
    在 :class:`.histogram` 的描述中定义了它们的格式。
    """
    if len(bins) + 1 != len(edges):
        raise ValueError("The length of bins must be one less than the length of edges.")
    
    area = 0.0
    for i in range(len(bins)):
        width = edges[i + 1] - edges[i]
        area += bins[i] * width
    
    return area