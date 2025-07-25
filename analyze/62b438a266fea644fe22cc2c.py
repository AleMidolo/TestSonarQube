def make_parsers():
    """
    Crear un analizador de nivel superior y sus subanalizadores, y devolverlos como una tupla.
    """
    import argparse

    # Crear el analizador principal
    parser = argparse.ArgumentParser(description='Analizador de comandos principal')
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')

    # Crear subanalizador para el comando 'add'
    parser_add = subparsers.add_parser('add', help='Agregar un nuevo elemento')
    parser_add.add_argument('name', help='Nombre del elemento')
    parser_add.add_argument('--value', '-v', help='Valor del elemento')

    # Crear subanalizador para el comando 'list' 
    parser_list = subparsers.add_parser('list', help='Listar elementos')
    parser_list.add_argument('--filter', '-f', help='Filtrar resultados')

    # Crear subanalizador para el comando 'delete'
    parser_delete = subparsers.add_parser('delete', help='Eliminar un elemento')
    parser_delete.add_argument('id', help='ID del elemento a eliminar')

    # Devolver una tupla con el parser principal y los subparsers
    return (parser, parser_add, parser_list, parser_delete)