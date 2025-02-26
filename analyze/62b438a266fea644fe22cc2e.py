import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y devuélvelos como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(description='Análisis de argumentos de línea de comandos.')
    
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Ejemplo de subparser
    subparser_a = subparsers.add_parser('subparser_a', help='Ayuda para subparser_a')
    subparser_a.add_argument('--option_a', type=str, help='Opción A para subparser_a')

    subparser_b = subparsers.add_parser('subparser_b', help='Ayuda para subparser_b')
    subparser_b.add_argument('--option_b', type=int, help='Opción B para subparser_b')

    # Analizar los argumentos
    args = parser.parse_args(unparsed_arguments)

    # Devolver un diccionario que mapea el nombre del subparser a su Namespace
    return {args.subparser_name: args}