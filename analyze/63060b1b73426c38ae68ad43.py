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
    
    # Create subparsers for spec command
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
        help='Template to use for spec file',
        default='default'
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

    # Add update command
    update_parser = spec_subparsers.add_parser(
        'update',
        help='Update spec file'
    )
    update_parser.add_argument(
        'spec_file',
        help='Path to spec file to update'
    )