def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Dato un insieme di argomenti e un dizionario che associa il nome di un sottoparser a un'istanza di `argparse.ArgumentParser`, consente a ciascun sottoparser richiesto di tentare di analizzare tutti gli argomenti. Questo permette di condividere argomenti comuni, come "--repository", tra più sottoparser.

    Restituisce il risultato come una tupla composta da (un dizionario che associa il nome del sottoparser a uno spazio dei nomi di argomenti analizzati, una lista di argomenti rimanenti non gestiti da alcun sottoparser).
    """
    parsed_results = {}
    remaining_arguments = unparsed_arguments[:]
    
    for name, parser in subparsers.items():
        try:
            parsed_args, remaining_arguments = parser.parse_known_args(remaining_arguments)
            parsed_results[name] = parsed_args
        except SystemExit:
            continue
    
    return parsed_results, remaining_arguments