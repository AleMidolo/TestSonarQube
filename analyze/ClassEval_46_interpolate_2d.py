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
        # Find the indices for bilinear interpolation
        # Find x indices
        x_idx = None
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x_idx = i
                break
        
        # Find y indices
        y_idx = None
        for j in range(len(y) - 1):
            if y[j] <= yi <= y[j + 1]:
                y_idx = j
                break
        
        # If point is outside the grid, handle edge cases
        if x_idx is None:
            if xi <= x[0]:
                x_idx = 0
            else:
                x_idx = len(x) - 2
        
        if y_idx is None:
            if yi <= y[0]:
                y_idx = 0
            else:
                y_idx = len(y) - 2
        
        # Get the four corner points
        x1, x2 = x[x_idx], x[x_idx + 1]
        y1, y2 = y[y_idx], y[y_idx + 1]
        
        z11 = z[x_idx][y_idx]
        z12 = z[x_idx][y_idx + 1]
        z21 = z[x_idx + 1][y_idx]
        z22 = z[x_idx + 1][y_idx + 1]
        
        # Bilinear interpolation
        # Normalize coordinates
        if x2 - x1 != 0:
            tx = (xi - x1) / (x2 - x1)
        else:
            tx = 0
        
        if y2 - y1 != 0:
            ty = (yi - y1) / (y2 - y1)
        else:
            ty = 0
        
        # Interpolate along x for both y values
        z_y1 = z11 * (1 - tx) + z21 * tx
        z_y2 = z12 * (1 - tx) + z22 * tx
        
        # Interpolate along y
        z_interp = z_y1 * (1 - ty) + z_y2 * ty
        
        result.append(z_interp)
    
    return result