def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to the main entry point.

    :param subparser: the subparser object to extend.
    """
    # Example implementation: Adding a command to the subparser
    parser = root_subparsers.add_parser('spec', help='Spec command options')
    parser.add_argument('--option1', type=str, help='Description for option1')
    parser.add_argument('--option2', type=int, help='Description for option2')
    # Add more options as needed