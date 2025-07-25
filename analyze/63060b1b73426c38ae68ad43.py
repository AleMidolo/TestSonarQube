def extend_cli(self, root_subparsers):
    """
    Agrega las opciones de línea de comandos (CLI) de especificación al punto de entrada principal.

    :param subparser: el objeto subparser que se va a extender.
    """
    # Create the parser for the "spec" command
    parser_spec = root_subparsers.add_parser(
        'spec',
        help='Manage API specifications'
    )

    # Create subparsers for spec command
    spec_subparsers = parser_spec.add_subparsers(
        title='spec commands',
        dest='spec_command'
    )

    # Add validate command
    validate_parser = spec_subparsers.add_parser(
        'validate',
        help='Validate an API specification'
    )
    validate_parser.add_argument(
        'spec_file',
        help='Path to the specification file'
    )

    # Add convert command
    convert_parser = spec_subparsers.add_parser(
        'convert',
        help='Convert specification between formats'
    )
    convert_parser.add_argument(
        'input_file',
        help='Input specification file'
    )
    convert_parser.add_argument(
        'output_file',
        help='Output specification file'
    )
    convert_parser.add_argument(
        '--from-format',
        choices=['yaml', 'json'],
        help='Input format (default: auto-detect)'
    )
    convert_parser.add_argument(
        '--to-format',
        choices=['yaml', 'json'],
        required=True,
        help='Output format'
    )