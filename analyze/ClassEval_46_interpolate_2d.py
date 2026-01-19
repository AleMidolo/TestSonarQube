@staticmethod
def interpolate_2d(x, y, z, x_interp, y_interp):
    """
    दो-आयामी डेटा का रैखिक अंतर्संवेदन
    :param x: डेटा बिंदु का x-निर्देशांक, सूची।
    :param y: डेटा बिंदु का y-निर्देशांक, सूची।
    :param z: डेटा बिंदु का z-निर्देशांक, सूची।
    :param x_interp: अंतर्संवेदन बिंदु का x-निर्देशांक, सूची।
    :param y_interp: अंतर्संवेदन बिंदु का y-निर्देशांक, सूची।
    :return: अंतर्संवेदन बिंदु का z-निर्देशांक, सूची।
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
        x1, x2 = x[x_idx], x[x_idx + 1]
        y1, y2 = y[y_idx], y[y_idx + 1]
        z11 = z[x_idx][y_idx]
        z12 = z[x_idx][y_idx + 1]
        z21 = z[x_idx + 1][y_idx]
        z22 = z[x_idx + 1][y_idx + 1]
        
        # Bilinear interpolation
        # Interpolate in x direction
        if x2 - x1 != 0:
            tx = (xi - x1) / (x2 - x1)
        else:
            tx = 0
        
        if y2 - y1 != 0:
            ty = (yi - y1) / (y2 - y1)
        else:
            ty = 0
        
        # Interpolate along y at x1 and x2
        z_y1 = z11 * (1 - ty) + z12 * ty
        z_y2 = z21 * (1 - ty) + z22 * ty
        
        # Interpolate along x
        z_interp = z_y1 * (1 - tx) + z_y2 * tx
        
        result.append(z_interp)
    
    return result