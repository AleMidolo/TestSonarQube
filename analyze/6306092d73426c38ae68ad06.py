def get_silent_args(self, args):
    """
    list of silenced argument

    :param args: The received arguments.
    :return: list, silenced argument names
    """
    silent_args = []
    for arg in args:
        if not args[arg]:
            silent_args.append(arg)
    return silent_args