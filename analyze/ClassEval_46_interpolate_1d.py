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
                    # y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
                    x0, x1 = x[i], x[i + 1]
                    y0, y1 = y[i], y[i + 1]
                    yi = y0 + (y1 - y0) * (xi - x0) / (x1 - x0)
                    result.append(yi)
                    break
    
    return result