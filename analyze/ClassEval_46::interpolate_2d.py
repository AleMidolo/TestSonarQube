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
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        x_idx = None
        y_idx = None
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x_idx = i
                break
        for j in range(len(y) - 1):
            if y[j] <= yi <= y[j + 1]:
                y_idx = j
                break
        if x_idx is None or y_idx is None:
            raise ValueError(f'Point ({xi}, {yi}) is outside the interpolation range')
        x1, x2 = (x[x_idx], x[x_idx + 1])
        y1, y2 = (y[y_idx], y[y_idx + 1])
        z11 = z[y_idx][x_idx]
        z12 = z[y_idx][x_idx + 1]
        z21 = z[y_idx + 1][x_idx]
        z22 = z[y_idx + 1][x_idx + 1]
        z_y1 = z11 + (z12 - z11) * (xi - x1) / (x2 - x1)
        z_y2 = z21 + (z22 - z21) * (xi - x1) / (x2 - x1)
        zi = z_y1 + (z_y2 - z_y1) * (yi - y1) / (y2 - y1)
        z_interp.append(zi)
    return z_interp