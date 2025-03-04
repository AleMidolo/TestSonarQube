def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to to the main entry point.
    
    :param subparser: the subparser object to extend.
    """
    # Create a subparser for spec commands
    spec_parser = root_subparsers.add_parser(
        'spec',
        help='Commands for working with specs'
    )
    
    # Create subparsers for the spec parser
    spec_subparsers = spec_parser.add_subparsers(dest='spec_command')
    
    # Add create command
    create_parser = spec_subparsers.add_parser(
        'create',
        help='Create a new spec file'
    )
    create_parser.add_argument(
        'name',
        help='Name of the spec to create'
    )
    
    # Add validate command
    validate_parser = spec_subparsers.add_parser(
        'validate', 
        help='Validate an existing spec file'
    )
    validate_parser.add_argument(
        'file',
        help='Path to spec file to validate'
    )
    
    # Add list command
    list_parser = spec_subparsers.add_parser(
        'list',
        help='List available specs'
    )