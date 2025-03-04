def validate_min_max_args(self, args):
    """
    检查给定参数的值是否在最小值和最大值之间

    检查参数的值是否在最小值和最大值之间
    :param args: 接收到的参数。
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'min_{arg_name}') and hasattr(self, f'max_{arg_name}'):
            min_val = getattr(self, f'min_{arg_name}')
            max_val = getattr(self, f'max_{arg_name}')
            
            if not isinstance(arg_value, (int, float)):
                raise TypeError(f"Parameter {arg_name} must be a number")
                
            if arg_value < min_val:
                raise ValueError(f"Parameter {arg_name} cannot be less than {min_val}")
                
            if arg_value > max_val:
                raise ValueError(f"Parameter {arg_name} cannot be greater than {max_val}")