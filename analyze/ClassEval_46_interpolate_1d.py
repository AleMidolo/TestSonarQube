def interpolate_1d(x, y, x_interp):
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
        # Find the two points that bracket xi
        if xi <= x[0]:
            # Extrapolate using first two points
            y_interp.append(y[0])
        elif xi >= x[-1]:
            # Extrapolate using last two points
            y_interp.append(y[-1])
        else:
            # Find the interval containing xi
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    # Linear interpolation formula
                    x0, x1 = x[i], x[i + 1]
                    y0, y1 = y[i], y[i + 1]
                    yi = y0 + (y1 - y0) * (xi - x0) / (x1 - x0)
                    y_interp.append(yi)
                    break
    
    return y_interp