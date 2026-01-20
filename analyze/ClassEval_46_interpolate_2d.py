@staticmethod
def interpolate_2d(x, y, z, x_interp, y_interp):
    """ 
    Interpolación lineal de datos bidimensionales
    :param x: La coordenada x del punto de datos, lista.
    :param y: La coordenada y del punto de datos, lista.
    :param z: La coordenada z del punto de datos, lista.
    :param x_interp: La coordenada x del punto de interpolación, lista.
    :param y_interp: La coordenada y del punto de interpolación, lista.
    :return: La coordenada z del punto de interpolación, lista.
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
        for j in range(len(y) - 1):
            if y[j] <= yi <= y[j + 1]:
                y_idx = j
                break
        
        # Get the four corner points
        x0, x1 = x[x_idx], x[x_idx + 1]
        y0, y1 = y[y_idx], y[y_idx + 1]
        
        z00 = z[x_idx][y_idx]
        z01 = z[x_idx][y_idx + 1]
        z10 = z[x_idx + 1][y_idx]
        z11 = z[x_idx + 1][y_idx + 1]
        
        # Bilinear interpolation
        # Interpolate in x direction
        if x1 - x0 != 0:
            tx = (xi - x0) / (x1 - x0)
        else:
            tx = 0
        
        if y1 - y0 != 0:
            ty = (yi - y0) / (y1 - y0)
        else:
            ty = 0
        
        # Interpolate along y at x0
        z_y0 = z00 * (1 - ty) + z01 * ty
        # Interpolate along y at x1
        z_y1 = z10 * (1 - ty) + z11 * ty
        # Interpolate along x
        z_interp = z_y0 * (1 - tx) + z_y1 * tx
        
        result.append(z_interp)
    
    return result