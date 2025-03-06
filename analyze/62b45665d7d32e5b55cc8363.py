def make_parsers():
    import argparse

    # Creazione del parser di livello superiore
    parser = argparse.ArgumentParser(description="Parser principale")

    # Creazione dei sottoparser
    subparsers = parser.add_subparsers(dest="command", help="Comandi disponibili")

    # Sottoparser per il comando 'foo'
    parser_foo = subparsers.add_parser('foo', help="Esegui il comando foo")
    parser_foo.add_argument('--bar', type=int, help="Parametro bar per il comando foo")

    # Sottoparser per il comando 'baz'
    parser_baz = subparsers.add_parser('baz', help="Esegui il comando baz")
    parser_baz.add_argument('--qux', type=str, help="Parametro qux per il comando baz")

    return parser, subparsers