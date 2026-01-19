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

    def find_segment(coord, value, coords):
        """Find the segment index where value lies between coords[i] and coords[i+1]"""
        for i in range(len(coords) - 1):
            if coords[i] <= value <= coords[i + 1]:
                return i
        if value < coords[0]:
            return 0
        else:
            return len(coords) - 2
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        i = find_segment('x', xi, x)
        j = find_segment('y', yi, y)
        x1, x2 = (x[i], x[i + 1])
        y1, y2 = (y[j], y[j + 1])
        z11 = z[j][i]
        z12 = z[j][i + 1]
        z21 = z[j + 1][i]
        z22 = z[j + 1][i + 1]
        z_y1 = z11 + (z12 - z11) * (xi - x1) / (x2 - x1)
        z_y2 = z21 + (z22 - z21) * (xi - x1) / (x2 - x1)
        zi = z_y1 + (z_y2 - z_y1) * (yi - y1) / (y2 - y1)
        z_interp.append(zi)
    return z_interp