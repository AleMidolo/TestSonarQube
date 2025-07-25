def validate_min_max_args(self, args):
    """
    检查给定参数的值是否在最小值和最大值之间

    检查参数的值是否在最小值和最大值之间
    :param args: 接收到的参数。
    """
    min_value = 0  # 假设最小值为0
    max_value = 100  # 假设最大值为100
    
    for arg in args:
        if not (min_value <= arg <= max_value):
            return False
    return True