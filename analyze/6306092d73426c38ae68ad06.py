def get_silent_args(self, args):
    """
    list of silenced argument

    :param args: The received arguments.
    :return: list, slienced argument names
    """
    silenced_args = []
    for arg in args:
        if arg.startswith('_'):
            silenced_args.append(arg)
    return silenced_args