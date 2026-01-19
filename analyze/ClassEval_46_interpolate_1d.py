def interpolate_1d(x, y, x_interp):
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
    result = []
    
    for xi in x_interp:
        # Handle edge cases
        if xi <= x[0]:
            result.append(y[0])
            continue
        if xi >= x[-1]:
            result.append(y[-1])
            continue
        
        # Find the two points that bracket xi
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                # Linear interpolation formula: y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
                x1, x2 = x[i], x[i + 1]
                y1, y2 = y[i], y[i + 1]
                yi = y1 + (y2 - y1) * (xi - x1) / (x2 - x1)
                result.append(yi)
                break
    
    return result