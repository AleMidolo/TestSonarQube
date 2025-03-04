def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Process command line arguments')
    
    # Add arguments to parser
    parser.add_argument('--input', '-i', type=str, help='Input file path')
    parser.add_argument('--output', '-o', type=str, help='Output file path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Increase output verbosity')
    
    # Parse arguments
    if len(arguments) > 0:
        args = parser.parse_args(arguments)
    else:
        args = parser.parse_args()
        
    return args