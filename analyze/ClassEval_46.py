class Interpolation:
    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        y_interp = []
        for xi in x_interp:
            yi = Interpolation._interpolate_1d_value(x, y, xi)
            if yi is not None:
                y_interp.append(yi)
        return y_interp

    @staticmethod
    def _interpolate_1d_value(x, y, xi):
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                return y[i] + (y[i + 1] - y[i]) * (xi - x[i]) / (x[i + 1] - x[i])
        return None

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            zi = Interpolation._interpolate_2d_value(x, y, z, xi, yi)
            if zi is not None:
                z_interp.append(zi)
        return z_interp

    @staticmethod
    def _interpolate_2d_value(x, y, z, xi, yi):
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                for j in range(len(y) - 1):
                    if y[j] <= yi <= y[j + 1]:
                        return Interpolation._bilinear_interpolation(z, i, j, xi, yi, x, y)
        return None

    @staticmethod
    def _bilinear_interpolation(z, i, j, xi, yi, x, y):
        z00 = z[i][j]
        z01 = z[i][j + 1]
        z10 = z[i + 1][j]
        z11 = z[i + 1][j + 1]
        return (z00 * (x[i + 1] - xi) * (y[j + 1] - yi) +
                z10 * (xi - x[i]) * (y[j + 1] - yi) +
                z01 * (x[i + 1] - xi) * (yi - y[j]) +
                z11 * (xi - x[i]) * (yi - y[j])) / ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))