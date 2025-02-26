import argparse

def parse_arguments(*unparsed_arguments):
    """
    Dado un conjunto de argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como un diccionario que mapea desde el nombre del subparser (o "global") a una instancia de `argparse.Namespace`.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Aquí se pueden agregar subcomandos y sus argumentos
    # Ejemplo de un subcomando
    subparser_a = subparsers.add_parser('comando_a')
    subparser_a.add_argument('--opcion', type=str, help='Una opción para comando_a')

    subparser_b = subparsers.add_parser('comando_b')
    subparser_b.add_argument('--otro', type=int, help='Otra opción para comando_b')

    # Analizar los argumentos
    args = parser.parse_args(unparsed_arguments)

    # Devolver los argumentos como un diccionario
    return {args.subparser_name: args}