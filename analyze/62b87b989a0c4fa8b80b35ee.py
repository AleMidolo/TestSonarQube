def reset(self):
    """
    当前上下文被重置为一个空字典，类的直方图桶（bins）将使用 *initial_value* 或 *make_bins()* 重新初始化。
    重置直方图。

    当前上下文被重置为一个空字典。
    直方图桶（bins）将根据初始化方式，使用 *initial_value* 或 *make_bins()* 重新初始化。
    """
    self.context = {}
    if hasattr(self, 'initial_value'):
        self.bins = [self.initial_value] * len(self.bins)
    elif hasattr(self, 'make_bins'):
        self.bins = self.make_bins()