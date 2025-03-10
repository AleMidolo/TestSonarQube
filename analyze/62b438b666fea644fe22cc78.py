import argparse

def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Example of adding arguments (customize as needed)
    parser.add_argument('-f', '--file', type=str, help='Input file path')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    
    return args