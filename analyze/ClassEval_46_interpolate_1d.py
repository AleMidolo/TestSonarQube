@staticmethod
def interpolate_1d(x, y, x_interp):
    """
        एक-आयामी डेटा का रैखिक अंतर्संवेदन
        :param x: डेटा बिंदु का x-निर्देशांक, सूची।
        :param y: डेटा बिंदु का y-निर्देशांक, सूची।
        :param x_interp: अंतर्संवेदन बिंदु का x-निर्देशांक, सूची।
        :return: अंतर्संवेदन बिंदु का y-निर्देशांक, सूची।
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