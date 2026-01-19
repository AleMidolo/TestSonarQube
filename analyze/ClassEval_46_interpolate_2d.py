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
        for i in range(len(x) - 1):
            for j in range(len(y) - 1):
                if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                    z11 = z[i][j]
                    z12 = z[i][j + 1]
                    z21 = z[i + 1][j]
                    z22 = z[i + 1][j + 1]
                    z_interp_value = (z11 * (x[i + 1] - xi) * (y[j + 1] - yi) + z21 * (xi - x[i]) * (y[j + 1] - yi) + z12 * (x[i + 1] - xi) * (yi - y[j]) + z22 * (xi - x[i]) * (yi - y[j])) / ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))
                    z_interp.append(z_interp_value)
                    break
    return z_interp