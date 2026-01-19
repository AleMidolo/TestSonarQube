@staticmethod
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

    def find_index(arr, value):
        """找到value在arr中的位置，返回左索引"""
        for i in range(len(arr) - 1):
            if arr[i] <= value <= arr[i + 1]:
                return i
        if value <= arr[0]:
            return 0
        else:
            return len(arr) - 2
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        i = find_index(x, xi)
        j = find_index(y, yi)
        z11 = z[j][i]
        z12 = z[j][i + 1]
        z21 = z[j + 1][i]
        z22 = z[j + 1][i + 1]
        z1 = z11 + (z12 - z11) * (xi - x[i]) / (x[i + 1] - x[i])
        z2 = z21 + (z22 - z21) * (xi - x[i]) / (x[i + 1] - x[i])
        zi = z1 + (z2 - z1) * (yi - y[j]) / (y[j + 1] - y[j])
        z_interp.append(zi)
    return z_interp