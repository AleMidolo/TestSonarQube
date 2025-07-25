def get_silent_args(self, args):
    """
    list of silenced argument

    :param args: The received arguments.
    :return: list, silenced argument names
    """
    silenced_args = []
    for arg in args:
        if not args[arg]:
            silenced_args.append(arg)
    return silenced_args