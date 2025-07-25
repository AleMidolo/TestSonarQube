def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Process command line arguments')
    
    # Add arguments to parser
    parser.add_argument('args', nargs='*', help='Command line arguments')
    
    # Parse arguments
    if len(arguments) > 0:
        # If arguments were passed to function, parse those
        args = parser.parse_args(arguments)
    else:
        # Otherwise parse sys.argv
        args = parser.parse_args()
        
    return args