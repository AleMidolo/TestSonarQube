def get_silent_args(self, args):
    """
    list of silenced argument

    :param args: The received arguments.
    :return: list, silenced argument names
    """
    silenced_args = []
    for arg in args:
        if arg.startswith('--silent-'):
            silenced_args.append(arg[len('--silent-'):])
    return silenced_args