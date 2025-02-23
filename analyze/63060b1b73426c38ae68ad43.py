def extend_cli(self, root_subparsers):
    """
    Agrega las opciones de línea de comandos (CLI) de especificación al punto de entrada principal.

    :param subparser: el objeto subparser que se va a extender.
    """
    # Crear un subcomando para la CLI
    parser = root_subparsers.add_parser('spec', help='Opciones de especificación')
    
    # Agregar opciones al subcomando
    parser.add_argument('--option1', type=str, help='Descripción de la opción 1')
    parser.add_argument('--option2', type=int, help='Descripción de la opción 2')
    parser.add_argument('--flag', action='store_true', help='Descripción de un flag')
    
    # Aquí se pueden agregar más opciones según sea necesario