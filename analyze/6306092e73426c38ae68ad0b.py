def validate_min_max_args(self, args):
    """
    检查给定参数的值是否在最小值和最大值之间

    检查参数的值是否在最小值和最大值之间
    :param args: 接收到的参数。
    """
    min_value = self.min_value  # 假设类中有最小值属性
    max_value = self.max_value  # 假设类中有最大值属性

    for arg in args:
        if not (min_value <= arg <= max_value):
            raise ValueError(f"参数 {arg} 超出范围 ({min_value}, {max_value})")
    return True