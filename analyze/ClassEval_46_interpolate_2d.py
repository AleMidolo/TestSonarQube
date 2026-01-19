def interpolate_2d(x, y, z, x_interp, y_interp):
    """
    二维数据的线性插值
    :param x: 数据点的 x 坐标，列表。
    :param y: 数据点的 y 坐标，列表。
    :param z: 数据点的 z 坐标，列表。
    :param x_interp: 插值点的 x 坐标，列表。
    :param y_interp: 插值点的 y 坐标，列表。
    :return: 插值点的 z 坐标，列表。
    >>> interpolation = Interpolation()
    >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
    [3.0, 7.0]

    """
    # Convert z to numpy array and flatten it
    z_array = np.array(z)

    # Create grid points from x and y
    points = []
    values = []

    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            points.append([xi, yj])
            values.append(z_array[i][j])

    points = np.array(points)
    values = np.array(values)

    # Create interpolator
    interpolator = LinearNDInterpolator(points, values)

    # Interpolate at the given points
    result = []
    for xi, yi in zip(x_interp, y_interp):
        z_val = interpolator(xi, yi)
        result.append(float(z_val))

    return result