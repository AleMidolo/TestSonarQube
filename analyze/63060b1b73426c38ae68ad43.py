def extend_cli(self, root_subparsers):
    """
    Agrega las opciones de línea de comandos (CLI) de especificación al punto de entrada principal.

    :param subparser: el objeto subparser que se va a extender.
    """
    spec_parser = root_subparsers.add_parser('spec', help='Comandos relacionados con la especificación.')
    spec_subparsers = spec_parser.add_subparsers(dest='spec_command', help='Comandos de especificación')

    # Ejemplo de subcomando para agregar una especificación
    add_spec_parser = spec_subparsers.add_parser('add', help='Agrega una nueva especificación.')
    add_spec_parser.add_argument('name', type=str, help='Nombre de la especificación.')
    add_spec_parser.add_argument('--description', type=str, help='Descripción de la especificación.', required=False)

    # Ejemplo de subcomando para listar especificaciones
    list_spec_parser = spec_subparsers.add_parser('list', help='Lista todas las especificaciones.')
    list_spec_parser.add_argument('--filter', type=str, help='Filtra las especificaciones por nombre.', required=False)

    # Ejemplo de subcomando para eliminar una especificación
    delete_spec_parser = spec_subparsers.add_parser('delete', help='Elimina una especificación.')
    delete_spec_parser.add_argument('name', type=str, help='Nombre de la especificación a eliminar.')