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

    # Add generate command  
    generate_parser = spec_subparsers.add_parser(
        'generate',
        help='Generate code from specification'
    )
    generate_parser.add_argument(
        'spec_file',
        help='Path to specification file'
    )
    generate_parser.add_argument(
        '-o', '--output',
        help='Output directory for generated code',
        default='.'
    )

    # Add list command
    list_parser = spec_subparsers.add_parser(
        'list',
        help='List available specifications'
    )