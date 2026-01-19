@staticmethod
def interpolate_2d(x, y, z, x_interp, y_interp):
    """
    Linear interpolation of two-dimensional data
    :param x: The x-coordinate of the data point, list.
    :param y: The y-coordinate of the data point, list.
    :param z: The z-coordinate of the data point, list.
    :param x_interp: The x-coordinate of the interpolation point, list.
    :param y_interp: The y-coordinate of the interpolation point, list.
    :return: The z-coordinate of the interpolation point, list.
    >>> interpolation = Interpolation()
    >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
    [3.0, 7.0]

    """
    result = []
    
    for xi, yi in zip(x_interp, y_interp):
        # Find the indices for interpolation
        # Find x indices
        x_idx = 0
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x_idx = i
                break
        
        # Find y indices
        y_idx = 0
        for i in range(len(y) - 1):
            if y[i] <= yi <= y[i + 1]:
                y_idx = i
                break
        
        # Get the four corner points
        x1, x2 = x[x_idx], x[x_idx + 1]
        y1, y2 = y[y_idx], y[y_idx + 1]
        
        z11 = z[x_idx][y_idx]
        z12 = z[x_idx][y_idx + 1]
        z21 = z[x_idx + 1][y_idx]
        z22 = z[x_idx + 1][y_idx + 1]
        
        # Bilinear interpolation
        # Interpolate in x direction
        if x2 - x1 != 0:
            z_y1 = z11 + (z21 - z11) * (xi - x1) / (x2 - x1)
            z_y2 = z12 + (z22 - z12) * (xi - x1) / (x2 - x1)
        else:
            z_y1 = z11
            z_y2 = z12
        
        # Interpolate in y direction
        if y2 - y1 != 0:
            z_interp = z_y1 + (z_y2 - z_y1) * (yi - y1) / (y2 - y1)
        else:
            z_interp = z_y1
        
        result.append(z_interp)
    
    return result