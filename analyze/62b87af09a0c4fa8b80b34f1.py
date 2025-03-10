def fill(self, coord, weight=1):
    """
    根据给定的 *weight* 在 *coord* 处填充直方图。

    超出直方图边界的坐标将被忽略。
    """
    if 0 <= coord < len(self.histogram):
        self.histogram[coord] += weight