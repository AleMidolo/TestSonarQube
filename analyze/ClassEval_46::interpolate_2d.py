class Interpolation: 
    def __init__(self):
        pass

    def interpolate_1d(self, x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :return: The y-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]
        """
        y_interp = []
        for xi in x_interp:
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    yi = y[i] + (y[i + 1] - y[i]) * (xi - x[i]) / (x[i + 1] - x[i])
                    y_interp.append(yi)
                    break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """ 
        Interpolazione lineare di dati bidimensionali
        :param x: La coordinata x del punto dati, lista.
        :param y: La coordinata y del punto dati, lista.
        :param z: La coordinata z del punto dati, lista.
        :param x_interp: La coordinata x del punto di interpolazione, lista.
        :param y_interp: La coordinata y del punto di interpolazione, lista.
        :return: La coordinata z del punto di interpolazione, lista.
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
                        z_interp_value = (z11 * (x[i + 1] - xi) * (y[j + 1] - yi) +
                                          z21 * (xi - x[i]) * (y[j + 1] - yi) +
                                          z12 * (x[i + 1] - xi) * (yi - y[j]) +
                                          z22 * (xi - x[i]) * (yi - y[j])) / \
                                          ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))
                        z_interp.append(z_interp_value)
                        break
        return z_interp