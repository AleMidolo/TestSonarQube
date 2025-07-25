def fill(self, coord, weight=1):
    """
    根据给定的 *weight* 在 *coord* 处填充直方图。

    超出直方图边界的坐标将被忽略。
    """
    if self.is_within_bounds(coord):
        self.histogram[coord] += weight

def is_within_bounds(self, coord):
    """
    检查给定的坐标是否在直方图的边界内。
    """
    return 0 <= coord < len(self.histogram)