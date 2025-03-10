def validate_min_max_args(self, args):
    """
    检查给定参数的值是否在最小值和最大值之间

    检查参数的值是否在最小值和最大值之间
    :param args: 接收到的参数。
    """
    if not hasattr(self, 'min_value') or not hasattr(self, 'max_value'):
        raise ValueError("min_value and max_value must be defined in the class.")
    
    for arg in args:
        if not (self.min_value <= arg <= self.max_value):
            return False
    return True