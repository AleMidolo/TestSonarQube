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
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                for j in range(len(y) - 1):
                    if y[j] <= yi <= y[j + 1]:
                        x1, x2 = (x[i], x[i + 1])
                        y1, y2 = (y[j], y[j + 1])
                        q11 = z[i][j]
                        q12 = z[i][j + 1]
                        q21 = z[i + 1][j]
                        q22 = z[i + 1][j + 1]
                        f_y1 = q11 + (q21 - q11) * (xi - x1) / (x2 - x1)
                        f_y2 = q12 + (q22 - q12) * (xi - x1) / (x2 - x1)
                        result = f_y1 + (f_y2 - f_y1) * (yi - y1) / (y2 - y1)
                        z_interp.append(result)
                        break
                break
    return z_interp