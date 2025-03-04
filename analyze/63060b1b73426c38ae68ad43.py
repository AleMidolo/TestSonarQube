def extend_cli(self, root_subparsers):
    """
    Agrega las opciones de línea de comandos (CLI) de especificación al punto de entrada principal.

    :param subparser: el objeto subparser que se va a extender.
    """
    # Create specification subparser
    spec_parser = root_subparsers.add_parser(
        'spec',
        help='Specification related commands'
    )
    
    # Create subparsers for spec commands
    spec_subparsers = spec_parser.add_subparsers(
        title='Specification commands',
        dest='spec_command'
    )

    # Add validate command
    validate_parser = spec_subparsers.add_parser(
        'validate',
        help='Validate a specification file'
    )
    validate_parser.add_argument(
        'spec_file',
        help='Path to specification file'
    )

    # Add create command  
    create_parser = spec_subparsers.add_parser(
        'create',
        help='Create a new specification file'
    )
    create_parser.add_argument(
        'output',
        help='Output path for new specification file'
    )

    # Add list command
    list_parser = spec_subparsers.add_parser(
        'list',
        help='List available specifications'
    )

    # Make spec_command required
    spec_parser.set_defaults(spec_command='list')