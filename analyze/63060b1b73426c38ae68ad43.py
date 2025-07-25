def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    # Example: Adding a new subcommand 'example' with an optional argument
    example_parser = root_subparsers.add_parser('example', help='Example command')
    example_parser.add_argument('--option', type=str, help='An example option')