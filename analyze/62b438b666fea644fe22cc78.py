import argparse

def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    parser = argparse.ArgumentParser(description="Parse command line arguments.")
    
    # Add arguments to the parser
    for arg in arguments:
        parser.add_argument(arg)
    
    # Parse the arguments
    args = parser.parse_args()
    
    return args