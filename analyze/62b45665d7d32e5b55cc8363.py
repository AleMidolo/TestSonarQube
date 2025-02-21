def make_parsers():
    import argparse

    # Creazione del parser di livello superiore
    main_parser = argparse.ArgumentParser(description='Parser di livello superiore')
    
    # Creazione di un sottoparser
    subparsers = main_parser.add_subparsers(dest='command', help='Comandi disponibili')

    # Esempio di sottoparser
    parser_a = subparsers.add_parser('comando_a', help='Esegui il comando A')
    parser_a.add_argument('--opzione', type=str, help='Opzione per il comando A')

    parser_b = subparsers.add_parser('comando_b', help='Esegui il comando B')
    parser_b.add_argument('--flag', action='store_true', help='Flag per il comando B')

    return main_parser, subparsers