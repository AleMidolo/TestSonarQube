def extend_cli(self, root_subparsers):
    """
    मुख्य एंट्री पॉइंट में स्पेक CLI विकल्प जोड़ता है।

    :param subparser: वह सबपार्सर ऑब्जेक्ट जिसे विस्तारित करना है।
    """
    # Add spec subcommand parser
    spec_parser = root_subparsers.add_parser(
        'spec',
        help='Manage project specifications'
    )

    # Create subparser for spec commands
    spec_subparsers = spec_parser.add_subparsers(
        title='spec commands',
        dest='spec_command'
    )

    # Add init command
    init_parser = spec_subparsers.add_parser(
        'init',
        help='Initialize a new spec file'
    )
    init_parser.add_argument(
        '--template',
        help='Template file to use for initialization'
    )

    # Add validate command  
    validate_parser = spec_subparsers.add_parser(
        'validate',
        help='Validate spec file'
    )
    validate_parser.add_argument(
        'spec_file',
        help='Path to spec file to validate'
    )

    # Add other common arguments
    for p in [init_parser, validate_parser]:
        p.add_argument(
            '--verbose', '-v',
            action='store_true',
            help='Enable verbose output'
        )