def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    # Esempio di aggiunta di un comando al subparser
    parser = root_subparsers.add_parser('example', help='Esempio di comando')
    parser.add_argument('--option', type=str, help='Un\'opzione per il comando esempio')
    
    # Aggiungere ulteriori opzioni o comandi qui