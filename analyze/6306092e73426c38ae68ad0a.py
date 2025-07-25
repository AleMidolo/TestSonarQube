def validate_choices_args(self, args):
    """
    检查给定参数的值是否是可用选项之一。

    :param args: 接收到的参数。

    检查选择参数的值是否是可用选项之一。
    :param args: 接收到的参数。
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("The class does not have a 'choices' attribute.")
    
    if not isinstance(self.choices, (list, tuple, set)):
        raise TypeError("The 'choices' attribute must be a list, tuple, or set.")
    
    if args not in self.choices:
        raise ValueError(f"The argument '{args}' is not a valid choice. Valid choices are: {self.choices}")
    
    return True