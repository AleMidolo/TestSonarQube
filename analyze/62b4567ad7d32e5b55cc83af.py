import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Example of adding arguments (customize as needed)
    parser.add_argument('-f', '--file', type=str, help="Path to the input file")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    
    return args