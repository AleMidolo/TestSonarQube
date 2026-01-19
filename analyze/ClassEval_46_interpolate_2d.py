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
        for i in range(len(coords) - 1):
            if coords[i] <= value <= coords[i + 1]:
                return (i, i + 1)
        return (None, None)

    def bilinear_interpolation(x_val, y_val, x1, x2, y1, y2, q11, q12, q21, q22):
        return (q11 * (x2 - x_val) * (y2 - y_val) + q21 * (x_val - x1) * (y2 - y_val) + q12 * (x2 - x_val) * (y_val - y1) + q22 * (x_val - x1) * (y_val - y1)) / ((x2 - x1) * (y2 - y1))
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        x_idx1, x_idx2 = find_segment('x', xi, x)
        y_idx1, y_idx2 = find_segment('y', yi, y)
        if x_idx1 is None or y_idx1 is None:
            raise ValueError(f'Interpolation point ({xi}, {yi}) is outside the data range')
        q11 = z[y_idx1][x_idx1]
        q12 = z[y_idx2][x_idx1]
        q21 = z[y_idx1][x_idx2]
        q22 = z[y_idx2][x_idx2]
        zi = bilinear_interpolation(xi, yi, x[x_idx1], x[x_idx2], y[y_idx1], y[y_idx2], q11, q12, q21, q22)
        z_interp.append(zi)
    return z_interp