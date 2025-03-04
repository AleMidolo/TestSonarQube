def extend_cli(self, root_subparsers):
    """
    मुख्य एंट्री पॉइंट में स्पेक CLI विकल्प जोड़ता है।

    :param subparser: वह सबपार्सर ऑब्जेक्ट जिसे विस्तारित करना है।
    """
    # Create spec subparser
    spec_parser = root_subparsers.add_parser(
        'spec',
        help='Manage project specifications'
    )

    # Add subcommands to spec parser
    spec_subparsers = spec_parser.add_subparsers(
        title='Commands',
        dest='spec_command'
    )

    # Add init command
    init_parser = spec_subparsers.add_parser(
        'init',
        help='Initialize a new specification'
    )
    init_parser.add_argument(
        '--name',
        help='Name of the specification',
        required=True
    )

    # Add validate command  
    validate_parser = spec_subparsers.add_parser(
        'validate',
        help='Validate an existing specification'
    )
    validate_parser.add_argument(
        '--path',
        help='Path to specification file',
        required=True
    )

    # Add list command
    list_parser = spec_subparsers.add_parser(
        'list',
        help='List all specifications'
    )