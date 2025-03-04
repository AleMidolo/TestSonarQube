def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    import argparse

    # Crear el analizador principal
    parser = argparse.ArgumentParser(description='Analizador de comandos principal')
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')

    # Crear subanalizador para el comando 'add'
    add_parser = subparsers.add_parser('add', help='Agregar un elemento')
    add_parser.add_argument('item', help='Elemento a agregar')
    add_parser.add_argument('--priority', type=int, default=1, help='Prioridad del elemento')

    # Crear subanalizador para el comando 'list' 
    list_parser = subparsers.add_parser('list', help='Listar elementos')
    list_parser.add_argument('--sort', choices=['asc', 'desc'], help='Ordenar elementos')

    # Crear subanalizador para el comando 'remove'
    remove_parser = subparsers.add_parser('remove', help='Eliminar un elemento')
    remove_parser.add_argument('id', type=int, help='ID del elemento a eliminar')

    return parser, add_parser, list_parser, remove_parser