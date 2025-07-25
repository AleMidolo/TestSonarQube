import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Aquí puedes agregar los argumentos que esperas recibir
    # Ejemplo:
    # parser.add_argument('-f', '--file', type=str, help='Path to the input file')
    
    # Parsear los argumentos
    args = parser.parse_args(arguments)
    
    return args