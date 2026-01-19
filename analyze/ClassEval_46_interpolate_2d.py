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
        """在有序数组arr中找到value所在的区间索引"""
        for i in range(len(arr) - 1):
            if arr[i] <= value <= arr[i + 1]:
                return i
        if value <= arr[0]:
            return 0
        else:
            return len(arr) - 2

    def bilinear_interpolation(x1, x2, y1, y2, z11, z12, z21, z22, x, y):
        """在矩形区域内进行双线性插值"""
        z_x1 = z11 + (z21 - z11) * (x - x1) / (x2 - x1)
        z_x2 = z12 + (z22 - z12) * (x - x1) / (x2 - x1)
        z_interp = z_x1 + (z_x2 - z_x1) * (y - y1) / (y2 - y1)
        return z_interp
    z_interp = []
    for xi, yi in zip(x_interp, y_interp):
        i = find_index(x, xi)
        j = find_index(y, yi)
        x1, x2 = (x[i], x[i + 1])
        y1, y2 = (y[j], y[j + 1])
        z11, z12 = (z[j][i], z[j][i + 1])
        z21, z22 = (z[j + 1][i], z[j + 1][i + 1])
        zi = bilinear_interpolation(x1, x2, y1, y2, z11, z12, z21, z22, xi, yi)
        z_interp.append(zi)
    return z_interp