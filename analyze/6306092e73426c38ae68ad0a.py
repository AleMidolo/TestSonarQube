def validate_choices_args(self, args):
    """
    检查给定参数的值是否是可用选项之一。

    :param args: 接收到的参数。

    检查选择参数的值是否是可用选项之一。
    :param args: 接收到的参数。
    """
    available_choices = self.get_available_choices()  # 假设有一个方法返回可用选项
    if args not in available_choices:
        raise ValueError(f"Invalid choice: {args}. Available choices are: {available_choices}")
    return True