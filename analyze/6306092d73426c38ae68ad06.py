def get_silent_args(self, args):
    silenced_args = []
    for arg in args:
        if arg.startswith('--silent-'):
            silenced_args.append(arg[len('--silent-'):])
    return silenced_args