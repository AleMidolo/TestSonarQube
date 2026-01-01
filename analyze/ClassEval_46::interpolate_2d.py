@staticmethod
def interpolate_2d(x, y, z, x_interp, y_interp):
    """ 
        Interpolazione lineare di dati bidimensionali
        :param x: La coordinata x del punto dati, lista.
        :param y: La coordinata y del punto dati, lista.
        :param z: La coordinata z del punto dati, lista.
        :param x_interp: La coordinata x del punto di interpolazione, lista.
        :param y_interp: La coordinata y del punto di interpolazione, lista.
        :return: La coordinata z del punto di interpolazione, lista.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]

        """
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    x_interp = np.array(x_interp)
    y_interp = np.array(y_interp)
    if z.shape != (len(x), len(y)):
        raise ValueError(f'z must have shape ({len(x)}, {len(y)}), but has shape {z.shape}')
    results = []
    for xi, yi in zip(x_interp, y_interp):
        x_idx = None
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x_idx = i
                break
        y_idx = None
        for j in range(len(y) - 1):
            if y[j] <= yi <= y[j + 1]:
                y_idx = j
                break
        if x_idx is None or y_idx is None:
            raise ValueError(f'Interpolation point ({xi}, {yi}) is outside the data range')
        x1, x2 = (x[x_idx], x[x_idx + 1])
        y1, y2 = (y[y_idx], y[y_idx + 1])
        Q11 = z[x_idx, y_idx]
        Q12 = z[x_idx, y_idx + 1]
        Q21 = z[x_idx + 1, y_idx]
        Q22 = z[x_idx + 1, y_idx + 1]
        R1 = Q11 + (Q21 - Q11) * (xi - x1) / (x2 - x1)
        R2 = Q12 + (Q22 - Q12) * (xi - x1) / (x2 - x1)
        result = R1 + (R2 - R1) * (yi - y1) / (y2 - y1)
        results.append(float(result))
    return results