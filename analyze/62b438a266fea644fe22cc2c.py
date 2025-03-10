import argparse

def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    # Crear el analizador de nivel superior
    parser = argparse.ArgumentParser(description="Analizador de nivel superior")
    
    # Crear subanalizadores
    subparsers = parser.add_subparsers(dest="command", help="Subcomandos disponibles")
    
    # Subanalizador para el comando 'foo'
    parser_foo = subparsers.add_parser('foo', help='Comando foo')
    parser_foo.add_argument('--bar', type=int, help='Argumento bar para foo')
    
    # Subanalizador para el comando 'baz'
    parser_baz = subparsers.add_parser('baz', help='Comando baz')
    parser_baz.add_argument('--qux', type=str, help='Argumento qux para baz')
    
    return parser, subparsers