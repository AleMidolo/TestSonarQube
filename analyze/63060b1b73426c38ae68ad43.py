def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to the main entry point.

    :param root_subparsers: the subparser object to extend.
    """
    spec_parser = root_subparsers.add_parser('spec', help='Manage specifications')
    spec_parser.add_argument('--list', action='store_true', help='List all specifications')
    spec_parser.add_argument('--add', type=str, help='Add a new specification')
    spec_parser.add_argument('--remove', type=str, help='Remove a specification')
    spec_parser.add_argument('--update', type=str, help='Update an existing specification')