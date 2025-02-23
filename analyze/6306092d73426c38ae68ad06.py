def get_silent_args(self, args):
    """
    list of silenced argument

    :param args: The received arguments.
    :return: list, silenced argument names
    """
    silenced_args = [arg for arg in args if arg.startswith('_')]
    return silenced_args