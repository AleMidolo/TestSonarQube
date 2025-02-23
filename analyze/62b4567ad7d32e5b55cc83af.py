import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser()
    
    # Aquí se pueden agregar los argumentos que se esperan
    parser.add_argument('--example', type=str, help='Un ejemplo de argumento')
    parser.add_argument('--count', type=int, help='Un número entero de ejemplo')
    
    # Analiza los argumentos proporcionados
    parsed_args = parser.parse_args(arguments)
    
    return parsed_args