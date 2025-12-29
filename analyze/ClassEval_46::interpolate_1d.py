def interpolate_1d(self, x, y, x_interp):
    """
        一维数据的线性插值
        :param x: 数据点的 x 坐标，列表。
        :param y: 数据点的 y 坐标，列表。
        :param x_interp: 插值点的 x 坐标，列表。
        :return: 插值点的 y 坐标，列表。
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
            if xi <= x[0]:
                y_interp.append(y[0])
            else:
                y_interp.append(y[-1])
    return y_interp