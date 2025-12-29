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
        """Find the segment index for interpolation in 1D"""
        for i in range(len(coords) - 1):
            if coords[i] <= value <= coords[i + 1]:
                return i
        if value < coords[0]:
            return 0
        else:
            return len(coords) - 2

    def bilinear_interpolation(x_val, y_val, x1, x2, y1, y2, z11, z12, z21, z22):
        """Perform bilinear interpolation within a grid cell"""
        z_x1 = z11 + (z21 - z11) * (x_val - x1) / (x2 - x1)
        z_x2 = z12 + (z22 - z12) * (x_val - x1) / (x2 - x1)
        z_interp = z_x1 + (z_x2 - z_x1) * (y_val - y1) / (y2 - y1)
        return z_interp
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        i = find_segment('x', xi, x)
        j = find_segment('y', yi, y)
        x1, x2 = (x[i], x[i + 1])
        y1, y2 = (y[j], y[j + 1])
        z11 = z[j][i]
        z12 = z[j + 1][i]
        z21 = z[j][i + 1]
        z22 = z[j + 1][i + 1]
        zi = bilinear_interpolation(xi, yi, x1, x2, y1, y2, z11, z12, z21, z22)
        z_interp.append(zi)
    return z_interp