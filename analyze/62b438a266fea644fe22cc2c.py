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
    add_parser.add_argument('--quantity', type=int, default=1, help='Cantidad a agregar')

    # Crear subanalizador para el comando 'remove' 
    remove_parser = subparsers.add_parser('remove', help='Eliminar un elemento')
    remove_parser.add_argument('item', help='Elemento a eliminar')
    remove_parser.add_argument('--quantity', type=int, default=1, help='Cantidad a eliminar')

    # Crear subanalizador para el comando 'list'
    list_parser = subparsers.add_parser('list', help='Listar elementos')
    list_parser.add_argument('--sort', action='store_true', help='Ordenar la lista')

    return parser, subparsers