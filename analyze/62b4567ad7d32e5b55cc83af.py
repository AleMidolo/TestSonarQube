import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser(description="Analiza los argumentos de línea de comandos.")
    
    # Aquí puedes agregar los argumentos que esperas recibir
    # Ejemplo:
    # parser.add_argument('-f', '--file', type=str, help='Archivo de entrada')
    
    # Si no se proporcionan argumentos, usa sys.argv por defecto
    if not arguments:
        import sys
        return parser.parse_args(sys.argv[1:])
    else:
        return parser.parse_args(arguments)