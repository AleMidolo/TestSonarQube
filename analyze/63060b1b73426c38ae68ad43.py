def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to to the main entry point.
    
    :param subparser: the subparser object to extend.
    """
    # Create spec subparser
    spec_parser = root_subparsers.add_parser(
        'spec',
        help='Commands for working with package specifications'
    )
    
    # Create subparser for spec commands
    spec_subparsers = spec_parser.add_subparsers(dest='spec_command')
    
    # Add create command
    create_parser = spec_subparsers.add_parser(
        'create',
        help='Create a new package specification'
    )
    create_parser.add_argument(
        'name',
        help='Name of the package specification'
    )
    create_parser.add_argument(
        '--template',
        help='Template to use for creating spec',
        default='default'
    )
    
    # Add list command
    list_parser = spec_subparsers.add_parser(
        'list',
        help='List available package specifications'
    )
    
    # Add validate command
    validate_parser = spec_subparsers.add_parser(
        'validate', 
        help='Validate a package specification'
    )
    validate_parser.add_argument(
        'spec_file',
        help='Path to specification file to validate'
    )