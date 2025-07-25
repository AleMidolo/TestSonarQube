def integral(bins, edges):
    """
    计算整体图形的面积
    计算积分（直方图的缩放比例）。

    *`bins`* 包含数值，*`edges`* 构成积分的网格。  
    在 :class:`.histogram` 的描述中定义了它们的格式。
    """
    total = 0.0
    for i in range(len(bins)):
        # 计算每个bin的宽度
        width = edges[i + 1] - edges[i]
        # 计算每个矩形的面积并累加
        total += bins[i] * width
    return total