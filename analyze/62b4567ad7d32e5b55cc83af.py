import argparse

def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    parser = argparse.ArgumentParser(description="Process some arguments.")
    
    # Example of adding arguments
    parser.add_argument('--input', type=str, help='Input file path')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    
    return args