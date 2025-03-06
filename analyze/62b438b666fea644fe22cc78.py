import argparse

def parse_arguments(*arguments):
    """
    Dado los argumentos de línea de comandos con los que se invocó este script, analiza los argumentos y los devuelve como una instancia de 'ArgumentParser'.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Example argument parsing, you can customize this based on your needs
    parser.add_argument('-f', '--file', type=str, help="Path to the input file.")
    parser.add_argument('-o', '--output', type=str, help="Path to the output file.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Increase output verbosity.")
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    
    return args