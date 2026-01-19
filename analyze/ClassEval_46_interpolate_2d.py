@staticmethod
def interpolate_2d(x, y, z, x_interp, y_interp):
    """
    二维数据的线性插值
    :param x: 数据点的 x 坐标，列表。
    :param y: 数据点的 y 坐标，列表。
    :param z: 数据点的 z 坐标，列表。
    :param x_interp: 插值点的 x 坐标，列表。
    :param y_interp: 插值点的 y 坐标，列表。
    :return: 插值点的 z 坐标，列表。
    >>> interpolation = Interpolation()
    >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
    [3.0, 7.0]

    """
    result = []
    
    for xi, yi in zip(x_interp, y_interp):
        # Find the bounding indices for x
        x_idx = None
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x_idx = i
                break
        
        # Find the bounding indices for y
        y_idx = None
        for j in range(len(y) - 1):
            if y[j] <= yi <= y[j + 1]:
                y_idx = j
                break
        
        # If point is outside bounds, handle edge cases
        if x_idx is None:
            x_idx = 0 if xi < x[0] else len(x) - 2
        if y_idx is None:
            y_idx = 0 if yi < y[0] else len(y) - 2
        
        # Get the four corner points
        x0, x1 = x[x_idx], x[x_idx + 1]
        y0, y1 = y[y_idx], y[y_idx + 1]
        
        z00 = z[x_idx][y_idx]
        z01 = z[x_idx][y_idx + 1]
        z10 = z[x_idx + 1][y_idx]
        z11 = z[x_idx + 1][y_idx + 1]
        
        # Bilinear interpolation
        # Normalize coordinates
        tx = (xi - x0) / (x1 - x0) if x1 != x0 else 0
        ty = (yi - y0) / (y1 - y0) if y1 != y0 else 0
        
        # Interpolate along x for both y values
        z_y0 = z00 * (1 - tx) + z10 * tx
        z_y1 = z01 * (1 - tx) + z11 * tx
        
        # Interpolate along y
        z_interp = z_y0 * (1 - ty) + z_y1 * ty
        
        result.append(z_interp)
    
    return result