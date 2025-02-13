def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to the main entry point.

    :param subparser: the subparser object to extend.
    """
    spec_parser = root_subparsers.add_parser('spec', help='Spec options')
    spec_parser.add_argument('--option1', type=str, help='Description for option1')
    spec_parser.add_argument('--option2', type=int, help='Description for option2')
    spec_parser.add_argument('--option3', action='store_true', help='Description for option3')