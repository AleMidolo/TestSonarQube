def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    parser = root_subparsers.add_parser(self.command_name, help=self.help_text)
    for option in self.options:
        parser.add_argument(option.name, **option.kwargs)