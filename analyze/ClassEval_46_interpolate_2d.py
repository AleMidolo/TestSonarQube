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

    def find_segment(coord, value, coord_list):
        for i in range(len(coord_list) - 1):
            if coord_list[i] <= value <= coord_list[i + 1]:
                return (i, i + 1)
        return None
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        x_segment = find_segment('x', xi, x)
        y_segment = find_segment('y', yi, y)
        if x_segment is None or y_segment is None:
            raise ValueError(f'Interpolation point ({xi}, {yi}) is outside the data range')
        i1, i2 = x_segment
        j1, j2 = y_segment
        x1, x2 = (x[i1], x[i2])
        y1, y2 = (y[j1], y[j2])
        z11 = z[j1][i1]
        z12 = z[j1][i2]
        z21 = z[j2][i1]
        z22 = z[j2][i2]
        z_y1 = z11 + (z12 - z11) * (xi - x1) / (x2 - x1)
        z_y2 = z21 + (z22 - z21) * (xi - x1) / (x2 - x1)
        z_interp_val = z_y1 + (z_y2 - z_y1) * (yi - y1) / (y2 - y1)
        z_interp.append(z_interp_val)
    return z_interp