def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Dato un insieme di argomenti e un dizionario che associa il nome di un sottoparser a un'istanza di `argparse.ArgumentParser`, consente a ciascun sottoparser richiesto di tentare di analizzare tutti gli argomenti. Questo permette di condividere argomenti comuni, come "--repository", tra più sottoparser.

    Restituisce il risultato come una tupla composta da (un dizionario che associa il nome del sottoparser a uno spazio dei nomi di argomenti analizzati, una lista di argomenti rimanenti non gestiti da alcun sottoparser).
    """
    parsed_args = {}
    remaining_args = unparsed_arguments.copy()
    
    # Try each subparser
    for name, subparser in subparsers.items():
        try:
            # Attempt to parse all remaining arguments
            parsed, remaining = subparser.parse_known_args(remaining_args)
            parsed_args[name] = parsed
            remaining_args = remaining
        except SystemExit:
            # Skip if parsing fails for this subparser
            continue
            
    return parsed_args, remaining_args