def interpolate_1d(self, x, y, x_interp):
    """
        Interpolación lineal de datos unidimensionales
        :param x: La coordenada x del punto de datos, lista.
        :param y: La coordenada y del punto de datos, lista.
        :param x_interp: La coordenada x del punto de interpolación, lista.
        :return: La coordenada y del punto de interpolación, lista.
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
        else:
            if xi < x[0]:
                yi = y[0] + (y[1] - y[0]) * (xi - x[0]) / (x[1] - x[0])
            else:
                yi = y[-2] + (y[-1] - y[-2]) * (xi - x[-2]) / (x[-1] - x[-2])
            y_interp.append(yi)
    return y_interp