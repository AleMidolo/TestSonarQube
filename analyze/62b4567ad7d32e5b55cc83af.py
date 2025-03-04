import argparse

def parse_arguments(*arguments):
    """
    Dati gli argomenti della riga di comando con cui è stato invocato questo script,
    analizza gli argomenti e restituiscili come un'istanza di ArgumentParser.
    """
    parser = argparse.ArgumentParser()
    
    # Aggiungi qui gli argomenti che desideri analizzare
    # Esempio: parser.add_argument('--example', help='Esempio di argomento')

    return parser.parse_args(arguments)