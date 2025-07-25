import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser(description="Analiza los argumentos de línea de comandos.")
    # Aquí puedes agregar los argumentos que necesites
    # Ejemplo: parser.add_argument('--input', type=str, help='Archivo de entrada')
    
    # Parsear los argumentos
    args = parser.parse_args(arguments)
    return args