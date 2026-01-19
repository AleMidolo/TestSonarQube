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
        # Find the four surrounding points for bilinear interpolation
        # Find indices for x
        x_idx = -1
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x_idx = i
                break
        
        # Find indices for y
        y_idx = -1
        for i in range(len(y) - 1):
            if y[i] <= yi <= y[i + 1]:
                y_idx = i
                break
        
        if x_idx == -1 or y_idx == -1:
            result.append(None)
            continue
        
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
            r1 = ((x2 - xi) * z11 + (xi - x1) * z21) / (x2 - x1)
            r2 = ((x2 - xi) * z12 + (xi - x1) * z22) / (x2 - x1)
        else:
            r1 = z11
            r2 = z12
        
        # Interpolate in y direction
        if y2 - y1 != 0:
            z_interp = ((y2 - yi) * r1 + (yi - y1) * r2) / (y2 - y1)
        else:
            z_interp = r1
        
        result.append(z_interp)
    
    return result