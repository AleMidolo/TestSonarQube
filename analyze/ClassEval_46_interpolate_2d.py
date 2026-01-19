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

    def find_interval(val, arr):
        """找到val在arr中的区间索引"""
        for i in range(len(arr) - 1):
            if arr[i] <= val <= arr[i + 1]:
                return i
        if val <= arr[0]:
            return 0
        else:
            return len(arr) - 2
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        i = find_interval(xi, x)
        j = find_interval(yi, y)
        z11 = z[j][i]
        z12 = z[j][i + 1]
        z21 = z[j + 1][i]
        z22 = z[j + 1][i + 1]
        if x[i + 1] != x[i]:
            tx = (xi - x[i]) / (x[i + 1] - x[i])
            z1 = z11 + (z12 - z11) * tx
            z2 = z21 + (z22 - z21) * tx
        else:
            z1 = z11
            z2 = z21
        if y[j + 1] != y[j]:
            ty = (yi - y[j]) / (y[j + 1] - y[j])
            zi = z1 + (z2 - z1) * ty
        else:
            zi = z1
        z_interp.append(zi)
    return z_interp