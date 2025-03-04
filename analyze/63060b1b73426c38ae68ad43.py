def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    parser = root_subparsers.add_parser(
        'run',
        help='Run the application'
    )
    
    parser.add_argument(
        '-c', '--config',
        help='Path to configuration file',
        default='config.yaml'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        help='Increase output verbosity',
        action='store_true'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0'
    )
    
    parser.set_defaults(func=self.run)