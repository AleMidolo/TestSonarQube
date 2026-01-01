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
    z = np.array(z)
    x_sorted = np.sort(np.unique(x))
    y_sorted = np.sort(np.unique(y))
    x_to_idx = {val: i for i, val in enumerate(x_sorted)}
    y_to_idx = {val: i for i, val in enumerate(y_sorted)}
    z_grid = np.zeros((len(y_sorted), len(x_sorted)))
    for i in range(len(x)):
        xi = x[i]
        yi = y[i]
        zi = z[i] if isinstance(z[i], (int, float)) else z[0][i]
        z_grid[y_to_idx[yi], x_to_idx[xi]] = zi
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        x_idx = np.searchsorted(x_sorted, xi) - 1
        y_idx = np.searchsorted(y_sorted, yi) - 1
        x_idx = max(0, min(x_idx, len(x_sorted) - 2))
        y_idx = max(0, min(y_idx, len(y_sorted) - 2))
        x1, x2 = (x_sorted[x_idx], x_sorted[x_idx + 1])
        y1, y2 = (y_sorted[y_idx], y_sorted[y_idx + 1])
        z11 = z_grid[y_idx, x_idx]
        z12 = z_grid[y_idx, x_idx + 1]
        z21 = z_grid[y_idx + 1, x_idx]
        z22 = z_grid[y_idx + 1, x_idx + 1]
        if x2 != x1:
            z_x1 = z11 + (z12 - z11) * (xi - x1) / (x2 - x1)
            z_x2 = z21 + (z22 - z21) * (xi - x1) / (x2 - x1)
        else:
            z_x1 = z11
            z_x2 = z21
        if y2 != y1:
            zi = z_x1 + (z_x2 - z_x1) * (yi - y1) / (y2 - y1)
        else:
            zi = z_x1
        z_interp.append(float(zi))
    return z_interp