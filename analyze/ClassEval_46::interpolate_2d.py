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
        x_idx = -1
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x_idx = i
                break
        y_idx = -1
        for j in range(len(y) - 1):
            if y[j] <= yi <= y[j + 1]:
                y_idx = j
                break
        if x_idx == -1 or y_idx == -1:
            continue
        z11 = z[x_idx][y_idx]
        z12 = z[x_idx][y_idx + 1]
        z21 = z[x_idx + 1][y_idx]
        z22 = z[x_idx + 1][y_idx + 1]
        if x[x_idx + 1] != x[x_idx]:
            rx = (xi - x[x_idx]) / (x[x_idx + 1] - x[x_idx])
            z_y1 = z11 + (z21 - z11) * rx
            z_y2 = z12 + (z22 - z12) * rx
        else:
            z_y1 = z11
            z_y2 = z12
        if y[y_idx + 1] != y[y_idx]:
            ry = (yi - y[y_idx]) / (y[y_idx + 1] - y[y_idx])
            zi = z_y1 + (z_y2 - z_y1) * ry
        else:
            zi = z_y1
        z_interp.append(zi)
    return z_interp