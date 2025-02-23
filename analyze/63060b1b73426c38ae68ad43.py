def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    # Example implementation: adding a command to the CLI
    parser = root_subparsers.add_parser('example_command', help='Esempio di comando')
    parser.add_argument('--option', type=str, help='Un\'opzione per il comando esempio')
    
    # You can add more commands and options as needed