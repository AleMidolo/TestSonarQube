def interpolate_1d(x, y, x_interp):
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
    result = []
    
    for xi in x_interp:
        # Find the two points that bracket xi
        if xi <= x[0]:
            # Extrapolate using first two points
            result.append(y[0])
        elif xi >= x[-1]:
            # Extrapolate using last two points
            result.append(y[-1])
        else:
            # Find the interval containing xi
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    # Linear interpolation formula
                    x0, x1 = x[i], x[i + 1]
                    y0, y1 = y[i], y[i + 1]
                    yi = y0 + (y1 - y0) * (xi - x0) / (x1 - x0)
                    result.append(yi)
                    break
    
    return result