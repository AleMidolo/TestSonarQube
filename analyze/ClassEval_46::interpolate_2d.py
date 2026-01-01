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
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        i = 0
        while i < len(x) - 1 and x[i] < xi:
            i += 1
        if i == 0:
            i = 1
        elif i == len(x):
            i = len(x) - 1
        j = 0
        while j < len(y) - 1 and y[j] < yi:
            j += 1
        if j == 0:
            j = 1
        elif j == len(y):
            j = len(y) - 1
        x1, x2 = (x[i - 1], x[i])
        y1, y2 = (y[j - 1], y[j])
        z11 = z[i - 1][j - 1]
        z12 = z[i - 1][j]
        z21 = z[i][j - 1]
        z22 = z[i][j]
        z_y1 = z11 + (z21 - z11) * (xi - x1) / (x2 - x1)
        z_y2 = z12 + (z22 - z12) * (xi - x1) / (x2 - x1)
        zi = z_y1 + (z_y2 - z_y1) * (yi - y1) / (y2 - y1)
        z_interp.append(zi)
    return z_interp