@staticmethod
def interpolate_1d(x, y, x_interp):
    """
        Interpolazione lineare di dati unidimensionali
        :param x: La coordinata x del punto dati, lista.
        :param y: La coordinata y del punto dati, lista.
        :param x_interp: La coordinata x del punto di interpolazione, lista.
        :return: La coordinata y del punto di interpolazione, lista.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]

        """
    y_interp = []
    for xi in x_interp:
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                yi = (y[i] * (x[i + 1] - xi) + y[i + 1] * (xi - x[i])) / (x[i + 1] - x[i])
                y_interp.append(yi)
                break
    return y_interp