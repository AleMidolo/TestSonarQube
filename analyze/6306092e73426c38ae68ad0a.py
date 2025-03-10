def validate_choices_args(self, args):
    """
    检查给定参数的值是否是可用选项之一。

    :param args: 接收到的参数。
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("The 'choices' attribute is not defined.")
    
    if not isinstance(self.choices, (list, tuple)):
        raise TypeError("The 'choices' attribute must be a list or tuple.")
    
    if args not in self.choices:
        raise ValueError(f"The argument '{args}' is not a valid choice. Valid choices are: {self.choices}")
    
    return True