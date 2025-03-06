import argparse

def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Example: Adding a positional argument
    parser.add_argument('input', type=str, help="Input file or directory")
    
    # Example: Adding an optional argument
    parser.add_argument('-o', '--output', type=str, help="Output file or directory", default="output.txt")
    
    # Example: Adding a flag
    parser.add_argument('-v', '--verbose', action='store_true', help="Increase output verbosity")
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    
    return args