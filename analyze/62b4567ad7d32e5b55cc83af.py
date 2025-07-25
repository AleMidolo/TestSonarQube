import argparse

def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Add arguments to the parser
    parser.add_argument('args', nargs='*', help="List of arguments passed to the script.")
    
    # Parse the arguments
    parsed_args = parser.parse_args(arguments)
    
    return parsed_args