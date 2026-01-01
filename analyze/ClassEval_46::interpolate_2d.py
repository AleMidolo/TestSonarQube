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
    for xp, yp in zip(x_interp, y_interp):
        i = 0
        while i < len(x) - 1 and x[i + 1] < xp:
            i += 1
        j = 0
        while j < len(y) - 1 and y[j + 1] < yp:
            j += 1
        i = min(i, len(x) - 2)
        j = min(j, len(y) - 2)
        x1, x2 = (x[i], x[i + 1])
        y1, y2 = (y[j], y[j + 1])
        z11 = z[j][i]
        z12 = z[j][i + 1]
        z21 = z[j + 1][i]
        z22 = z[j + 1][i + 1]
        z_y1 = z11 + (z12 - z11) * (xp - x1) / (x2 - x1)
        z_y2 = z21 + (z22 - z21) * (xp - x1) / (x2 - x1)
        z_interp_val = z_y1 + (z_y2 - z_y1) * (yp - y1) / (y2 - y1)
        z_interp.append(z_interp_val)
    return z_interp