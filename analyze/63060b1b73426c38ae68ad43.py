def extend_cli(self, root_subparsers):
    """
    Agrega las opciones de línea de comandos (CLI) de especificación al punto de entrada principal.

    :param root_subparsers: el objeto subparser que se va a extender.
    """
    # Ejemplo de cómo agregar un subparser para un comando específico
    spec_parser = root_subparsers.add_parser('especificacion', help='Comandos relacionados con la especificación')
    spec_parser.add_argument('--opcion1', type=str, help='Descripción de la opción 1')
    spec_parser.add_argument('--opcion2', type=int, help='Descripción de la opción 2')
    spec_parser.set_defaults(func=self.handle_especificacion)

def handle_especificacion(self, args):
    """
    Maneja el comando de especificación.

    :param args: Argumentos pasados desde la línea de comandos.
    """
    if args.opcion1:
        print(f"Opción 1 seleccionada: {args.opcion1}")
    if args.opcion2:
        print(f"Opción 2 seleccionada: {args.opcion2}")