import argparse

def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Example of adding arguments to the parser
    parser.add_argument('-f', '--file', type=str, help="Path to the input file")
    parser.add_argument('-v', '--verbose', action='store_true', help="Increase output verbosity")
    
    # Parse the arguments
    args = parser.parse_args(arguments)
    
    return args