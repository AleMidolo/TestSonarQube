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

    def find_index(arr, val):
        """Find the index i such that arr[i] <= val <= arr[i+1]"""
        for i in range(len(arr) - 1):
            if arr[i] <= val <= arr[i + 1]:
                return i
        return None

    def bilinear_interpolation(x1, x2, y1, y2, z11, z12, z21, z22, x, y):
        """Perform bilinear interpolation"""
        z_x1 = z11 + (z21 - z11) * (x - x1) / (x2 - x1)
        z_x2 = z12 + (z22 - z12) * (x - x1) / (x2 - x1)
        z_interp = z_x1 + (z_x2 - z_x1) * (y - y1) / (y2 - y1)
        return z_interp
    z_interp_results = []
    for xi, yi in zip(x_interp, y_interp):
        x_idx = find_index(x, xi)
        if x_idx is None:
            raise ValueError(f'x value {xi} is outside the range of x data')
        y_idx = find_index(y, yi)
        if y_idx is None:
            raise ValueError(f'y value {yi} is outside the range of y data')
        x1, x2 = (x[x_idx], x[x_idx + 1])
        y1, y2 = (y[y_idx], y[y_idx + 1])
        z11 = z[y_idx][x_idx]
        z12 = z[y_idx][x_idx + 1]
        z21 = z[y_idx + 1][x_idx]
        z22 = z[y_idx + 1][x_idx + 1]
        z_interp = bilinear_interpolation(x1, x2, y1, y2, z11, z12, z21, z22, xi, yi)
        z_interp_results.append(z_interp)
    return z_interp_results