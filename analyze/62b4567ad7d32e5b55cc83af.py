import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser()
    
    # Aquí puedes agregar los argumentos que deseas analizar
    parser.add_argument('--example', type=str, help='Un ejemplo de argumento')
    parser.add_argument('--count', type=int, default=1, help='Un contador de ejemplo')
    
    # Analiza los argumentos
    parsed_args = parser.parse_args(arguments)
    
    return parsed_args