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
    if not isinstance(z[0], list):
        raise ValueError('z must be a 2D list')
    for xp, yp in zip(x_interp, y_interp):
        x_idx = -1
        for i in range(len(x) - 1):
            if x[i] <= xp <= x[i + 1]:
                x_idx = i
                break
        y_idx = -1
        for j in range(len(y) - 1):
            if y[j] <= yp <= y[j + 1]:
                y_idx = j
                break
        if x_idx == -1 or y_idx == -1:
            raise ValueError(f'Interpolation point ({xp}, {yp}) is outside the data range')
        z11 = z[y_idx][x_idx]
        z12 = z[y_idx][x_idx + 1]
        z21 = z[y_idx + 1][x_idx]
        z22 = z[y_idx + 1][x_idx + 1]
        z1 = z11 + (z12 - z11) * (xp - x[x_idx]) / (x[x_idx + 1] - x[x_idx])
        z2 = z21 + (z22 - z21) * (xp - x[x_idx]) / (x[x_idx + 1] - x[x_idx])
        zp = z1 + (z2 - z1) * (yp - y[y_idx]) / (y[y_idx + 1] - y[y_idx])
        z_interp.append(zp)
    return z_interp