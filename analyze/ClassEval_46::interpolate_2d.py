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
            raise ValueError('Interpolation point outside data range')
        z11 = z[x_idx][y_idx]
        z12 = z[x_idx][y_idx + 1]
        z21 = z[x_idx + 1][y_idx]
        z22 = z[x_idx + 1][y_idx + 1]
        dx = x[x_idx + 1] - x[x_idx]
        dy = y[y_idx + 1] - y[y_idx]
        if dx == 0 or dy == 0:
            raise ValueError('Division by zero in interpolation')
        tx = (xi - x[x_idx]) / dx
        ty = (yi - y[y_idx]) / dy
        z_interp_y1 = z11 + (z21 - z11) * tx
        z_interp_y2 = z12 + (z22 - z12) * tx
        z_interp_val = z_interp_y1 + (z_interp_y2 - z_interp_y1) * ty
        z_interp.append(z_interp_val)
    return z_interp