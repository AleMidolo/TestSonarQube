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
        i = 0
        while i < len(x) - 1 and x[i + 1] < xi:
            i += 1
        j = 0
        while j < len(y) - 1 and y[j + 1] < yi:
            j += 1
        if i >= len(x) - 1:
            i = len(x) - 2
        if j >= len(y) - 1:
            j = len(y) - 2
        x1, x2 = (x[i], x[i + 1])
        y1, y2 = (y[j], y[j + 1])
        z11 = z[j][i]
        z12 = z[j][i + 1]
        z21 = z[j + 1][i]
        z22 = z[j + 1][i + 1]
        z_y1 = z11 + (z12 - z11) * (xi - x1) / (x2 - x1)
        z_y2 = z21 + (z22 - z21) * (xi - x1) / (x2 - x1)
        z_interp_val = z_y1 + (z_y2 - z_y1) * (yi - y1) / (y2 - y1)
        z_interp.append(z_interp_val)
    return z_interp