def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    # Example implementation: adding a command to the CLI
    parser = root_subparsers.add_parser('example', help='Esempio di comando')
    parser.add_argument('--option', type=str, help='Un\'opzione per il comando esempio')
    parser.set_defaults(func=self.example_command)

def example_command(self, args):
    # Example command implementation
    print(f'Eseguito il comando esempio con opzione: {args.option}')