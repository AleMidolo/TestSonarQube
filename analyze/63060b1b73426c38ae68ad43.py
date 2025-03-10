def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    # Example: Adding a new subcommand 'example' with its own arguments
    example_parser = root_subparsers.add_parser('example', help='Example command')
    example_parser.add_argument('--option1', type=str, help='Example option 1')
    example_parser.add_argument('--option2', type=int, help='Example option 2')