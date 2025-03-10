def extend_cli(self, root_subparsers):
    """
    Agrega las opciones de línea de comandos (CLI) de especificación al punto de entrada principal.

    :param root_subparsers: el objeto subparser que se va a extender.
    """
    spec_parser = root_subparsers.add_parser('spec', help='Opciones de especificación')
    spec_parser.add_argument('--input', type=str, required=True, help='Archivo de entrada para la especificación')
    spec_parser.add_argument('--output', type=str, required=True, help='Archivo de salida para la especificación')
    spec_parser.add_argument('--verbose', action='store_true', help='Habilita el modo verboso')