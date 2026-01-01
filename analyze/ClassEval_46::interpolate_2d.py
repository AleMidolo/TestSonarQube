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
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    z = np.array(z, dtype=float)
    if z.shape != (len(y), len(x)):
        raise ValueError(f'z must have shape ({len(y)}, {len(x)}), but has shape {z.shape}')
    z_interp = []
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
            raise ValueError(f'Point ({xi}, {yi}) is outside the interpolation grid')
        x1, x2 = (x[x_idx], x[x_idx + 1])
        y1, y2 = (y[y_idx], y[y_idx + 1])
        z11 = z[y_idx, x_idx]
        z12 = z[y_idx, x_idx + 1]
        z21 = z[y_idx + 1, x_idx]
        z22 = z[y_idx + 1, x_idx + 1]
        wx = (xi - x1) / (x2 - x1)
        wy = (yi - y1) / (y2 - y1)
        z_interp_val = (1 - wx) * (1 - wy) * z11 + wx * (1 - wy) * z12 + (1 - wx) * wy * z21 + wx * wy * z22
        z_interp.append(float(z_interp_val))
    return z_interp