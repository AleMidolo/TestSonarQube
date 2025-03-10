import argparse

def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    # Crear el analizador de nivel superior
    parser = argparse.ArgumentParser(description='Analizador de nivel superior')
    
    # Crear subanalizadores
    subparsers = parser.add_subparsers(dest='command', help='Subcomandos')
    
    # Subanalizador 1
    parser_a = subparsers.add_parser('comando_a', help='Descripción del comando A')
    parser_a.add_argument('arg1', type=str, help='Argumento 1 del comando A')
    
    # Subanalizador 2
    parser_b = subparsers.add_parser('comando_b', help='Descripción del comando B')
    parser_b.add_argument('arg2', type=int, help='Argumento 2 del comando B')
    
    return parser, subparsers