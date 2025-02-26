def fill(self, coord, weight=1):
    """
    根据给定的 *weight* 在 *coord* 处填充直方图。

    超出直方图边界的坐标将被忽略。
    """
    x, y = coord
    if 0 <= x < self.width and 0 <= y < self.height:
        self.histogram[y][x] += weight