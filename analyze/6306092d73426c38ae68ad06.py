def get_silent_args(self, args):
    """
    被静默的参数列表

    :param args: 接收到的参数。
    :return: list，被静默的参数名称列表。
    """
    silent_args = []
    for arg in args:
        if isinstance(arg, dict) and arg.get('silent', False):
            silent_args.append(arg.get('name'))
    return silent_args