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
        # Find the surrounding points
        for i in range(len(x) - 1):
            for j in range(len(y) - 1):
                if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                    # Perform bilinear interpolation
                    z11 = z[i][j]
                    z12 = z[i][j + 1]
                    z21 = z[i + 1][j]
                    z22 = z[i + 1][j + 1]
                    z_interp.append(
                        (z11 * (x[i + 1] - xi) * (y[j + 1] - yi) +
                         z21 * (xi - x[i]) * (y[j + 1] - yi) +
                         z12 * (x[i + 1] - xi) * (yi - y[j]) +
                         z22 * (xi - x[i]) * (yi - y[j])) /
                        ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))
                    )
                    break
    return z_interp