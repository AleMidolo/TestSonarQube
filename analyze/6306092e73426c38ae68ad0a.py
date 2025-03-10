def validate_choices_args(self, args):
    """
    检查给定参数的值是否是可用选项之一。

    :param args: 接收到的参数。
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("The class does not have a 'choices' attribute.")
    
    if not isinstance(self.choices, (list, tuple, set)):
        raise TypeError("The 'choices' attribute must be a list, tuple, or set.")
    
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"Invalid choice: {arg}. Valid choices are: {self.choices}")
    
    return True