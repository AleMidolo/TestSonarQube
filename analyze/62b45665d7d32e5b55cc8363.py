def make_parsers():
    """
    Crea un analizador de nivel superior y sus subanalizadores, y devuélvalos como una tupla.
    """
    import argparse

    # Crear el parser principal
    parser = argparse.ArgumentParser(description='Sistema de gestión de tareas')
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')

    # Subparser para agregar tarea
    add_parser = subparsers.add_parser('add', help='Agregar una nueva tarea')
    add_parser.add_argument('title', help='Título de la tarea')
    add_parser.add_argument('-d', '--description', help='Descripción de la tarea')
    add_parser.add_argument('-p', '--priority', type=int, choices=[1,2,3], 
                           help='Prioridad de la tarea (1-3)')

    # Subparser para listar tareas
    list_parser = subparsers.add_parser('list', help='Listar todas las tareas')
    list_parser.add_argument('-s', '--status', choices=['pending', 'completed'],
                            help='Filtrar por estado')
    
    # Subparser para completar tarea
    complete_parser = subparsers.add_parser('complete', help='Marcar tarea como completada')
    complete_parser.add_argument('task_id', type=int, help='ID de la tarea')

    # Subparser para eliminar tarea
    delete_parser = subparsers.add_parser('delete', help='Eliminar una tarea')
    delete_parser.add_argument('task_id', type=int, help='ID de la tarea')

    return parser, subparsers