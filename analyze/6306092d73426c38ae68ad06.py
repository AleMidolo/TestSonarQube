def get_silent_args(self, args):
    """
    被静默的参数列表


    :param args: 接收到的参数。
    :return: list，被静默的参数名称列表。
    """
    silent_args = []
    for arg in args:
        if isinstance(arg, str) and arg.startswith('_'):
            silent_args.append(arg)
    return silent_args