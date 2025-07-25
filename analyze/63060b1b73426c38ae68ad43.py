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
        help='Name of the specification to create'
    )
    
    # Add list command
    list_parser = spec_subparsers.add_parser(
        'list',
        help='List available package specifications'
    )
    
    # Add edit command
    edit_parser = spec_subparsers.add_parser(
        'edit',
        help='Edit an existing package specification'
    )
    edit_parser.add_argument(
        'name',
        help='Name of the specification to edit'
    )
    
    # Add delete command
    delete_parser = spec_subparsers.add_parser(
        'delete',
        help='Delete a package specification'
    )
    delete_parser.add_argument(
        'name',
        help='Name of the specification to delete'
    )