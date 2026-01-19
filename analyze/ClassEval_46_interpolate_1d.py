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
        # 找到 xi 所在的区间
        if xi <= x[0]:
            # 如果 xi 小于等于最小的 x，使用第一个点的 y 值
            result.append(y[0])
        elif xi >= x[-1]:
            # 如果 xi 大于等于最大的 x，使用最后一个点的 y 值
            result.append(y[-1])
        else:
            # 找到 xi 所在的区间 [x[i], x[i+1]]
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    # 线性插值公式: y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
                    x0, x1 = x[i], x[i + 1]
                    y0, y1 = y[i], y[i + 1]
                    yi = y0 + (y1 - y0) * (xi - x0) / (x1 - x0)
                    result.append(yi)
                    break
    
    return result