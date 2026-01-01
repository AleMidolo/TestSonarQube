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
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        for i in range(len(x) - 1):
            for j in range(len(y) - 1):
                if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                    z11 = z[i][j]
                    z12 = z[i][j + 1]
                    z21 = z[i + 1][j]
                    z22 = z[i + 1][j + 1]
                    z_interp.append((z11 * (x[i + 1] - xi) * (y[j + 1] - yi) + z21 * (xi - x[i]) * (y[j + 1] - yi) + z12 * (x[i + 1] - xi) * (yi - y[j]) + z22 * (xi - x[i]) * (yi - y[j])) / ((x[i + 1] - x[i]) * (y[j + 1] - y[j])))
                    break
    return z_interp