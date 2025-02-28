import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    # Add your argument parsing logic here
    # Example: parser.add_argument('--example', type=str, help='An example argument')
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    return args