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
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    x_interp = np.array(x_interp)
    y_interp = np.array(y_interp)
    if z.shape != (len(x), len(y)):
        raise ValueError('z must be a 2D array with shape (len(x), len(y))')
    results = []
    for xi, yi in zip(x_interp, y_interp):
        i = np.searchsorted(x, xi) - 1
        j = np.searchsorted(y, yi) - 1
        i = max(0, min(i, len(x) - 2))
        j = max(0, min(j, len(y) - 2))
        x1, x2 = (x[i], x[i + 1])
        y1, y2 = (y[j], y[j + 1])
        z11 = z[i, j]
        z12 = z[i, j + 1]
        z21 = z[i + 1, j]
        z22 = z[i + 1, j + 1]
        z_y1 = z11 + (z21 - z11) * (xi - x1) / (x2 - x1)
        z_y2 = z12 + (z22 - z12) * (xi - x1) / (x2 - x1)
        z_interp = z_y1 + (z_y2 - z_y1) * (yi - y1) / (y2 - y1)
        results.append(float(z_interp))
    return results