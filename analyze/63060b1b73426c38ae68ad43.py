def extend_cli(self, root_subparsers):
    """
    Aggiunge le opzioni CLI specifiche al punto di ingresso principale.

    :param subparser: l'oggetto subparser da estendere.
    """
    # Esempio di aggiunta di un comando al subparser
    parser = root_subparsers.add_parser('comando', help='Descrizione del comando')
    parser.add_argument('--opzione', type=str, help='Descrizione dell\'opzione')
    parser.set_defaults(func=self.some_function)

def some_function(self, args):
    # Implementazione della funzione da chiamare quando il comando viene eseguito
    print(f"Eseguito il comando con opzione: {args.opzione}")