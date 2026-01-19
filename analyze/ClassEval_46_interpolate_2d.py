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
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        x1, x2 = (None, None)
        y1, y2 = (None, None)
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x1, x2 = (x[i], x[i + 1])
                y1, y2 = (y[i], y[i + 1])
                break
        if x1 is not None and x2 is not None:
            z1 = z[y.index(y1)][x.index(x1)] + (z[y.index(y1)][x.index(x2)] - z[y.index(y1)][x.index(x1)]) * (xi - x1) / (x2 - x1)
            z2 = z[y.index(y2)][x.index(x1)] + (z[y.index(y2)][x.index(x2)] - z[y.index(y2)][x.index(x1)]) * (xi - x1) / (x2 - x1)
            z_interp.append(z1 + (z2 - z1) * (yi - y1) / (y2 - y1))
    return z_interp