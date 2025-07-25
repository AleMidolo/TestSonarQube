def validate_min_max_args(self, args):
    """
    检查给定参数的值是否在最小值和最大值之间

    检查参数的值是否在最小值和最大值之间
    :param args: 接收到的参数。
    """
    min_value = self.min_value  # 假设最小值存储在实例变量中
    max_value = self.max_value  # 假设最大值存储在实例变量中

    for arg in args:
        if not (min_value <= arg <= max_value):
            return False
    return True