@staticmethod
def interpolate_2d(x, y, z, x_interp, y_interp):
    """ 
        Interpolación lineal de datos bidimensionales
        :param x: La coordenada x del punto de datos, lista.
        :param y: La coordenada y del punto de datos, lista.
        :param z: La coordenada z del punto de datos, lista.
        :param x_interp: La coordenada x del punto de interpolación, lista.
        :param y_interp: La coordenada y del punto de interpolación, lista.
        :return: La coordenada z del punto de interpolación, lista.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]

        """
    import numpy as np
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    z = np.array(z, dtype=float)
    x_interp = np.array(x_interp, dtype=float)
    y_interp = np.array(y_interp, dtype=float)
    if z.shape != (len(x), len(y)):
        raise ValueError('z must be a 2D array with shape (len(x), len(y))')
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
            raise ValueError(f'Interpolation point ({xi}, {yi}) is outside the grid')
        z00 = z[x_idx, y_idx]
        z01 = z[x_idx, y_idx + 1]
        z10 = z[x_idx + 1, y_idx]
        z11 = z[x_idx + 1, y_idx + 1]
        tx = (xi - x[x_idx]) / (x[x_idx + 1] - x[x_idx])
        ty = (yi - y[y_idx]) / (y[y_idx + 1] - y[y_idx])
        z0 = z00 * (1 - ty) + z01 * ty
        z1 = z10 * (1 - ty) + z11 * ty
        zi = z0 * (1 - tx) + z1 * tx
        results.append(float(zi))
    return results