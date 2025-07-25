def validate_choices_args(self, args):
    """
    检查给定参数的值是否是可用选项之一。

    :param args: 接收到的参数。

    检查选择参数的值是否是可用选项之一。
    :param args: 接收到的参数。
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, 'choices') and arg_name in self.choices:
            valid_choices = self.choices[arg_name]
            if arg_value not in valid_choices:
                raise ValueError(f"Invalid value '{arg_value}' for argument '{arg_name}'. "
                               f"Valid choices are: {valid_choices}")