def get_silent_args(self, args):
    """
    被静默的参数列表

    :param args: 接收到的参数。
    :return: list，被静默的参数名称列表。
    """
    silent_args = []
    for arg_name, arg_value in args.items():
        if arg_value is None:
            silent_args.append(arg_name)
    return silent_args