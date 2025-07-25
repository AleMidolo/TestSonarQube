def extend_cli(self, root_subparsers):
    """
    Agrega las opciones de línea de comandos (CLI) de especificación al punto de entrada principal.

    :param subparser: el objeto subparser que se va a extender.
    """
    spec_parser = root_subparsers.add_parser('spec', help='Comandos relacionados con la especificación.')
    spec_parser.add_argument('--list', action='store_true', help='Listar todas las especificaciones disponibles.')
    spec_parser.add_argument('--add', type=str, help='Agregar una nueva especificación.')
    spec_parser.add_argument('--remove', type=str, help='Eliminar una especificación existente.')