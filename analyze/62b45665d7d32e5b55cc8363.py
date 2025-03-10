def make_parsers():
    """
    Crea un parser di livello superiore e i suoi sottoparser e restituiscili come una tupla.
    """
    import argparse

    # Creazione del parser principale
    parser = argparse.ArgumentParser(description="Parser principale")

    # Creazione dei sottoparser
    subparsers = parser.add_subparsers(dest="command", help="Comandi disponibili")

    # Sottoparser per il comando 'foo'
    parser_foo = subparsers.add_parser('foo', help='Esegui il comando foo')
    parser_foo.add_argument('--bar', type=int, help='Argomento bar per foo')

    # Sottoparser per il comando 'baz'
    parser_baz = subparsers.add_parser('baz', help='Esegui il comando baz')
    parser_baz.add_argument('--qux', type=str, help='Argomento qux per baz')

    return parser, subparsers