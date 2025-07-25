import yaml

class IRValidatorException(Exception):
    pass

def validate_from_file(cls, yaml_file=None):
    """
    Carica e valida che un file YAML contenga tutti i campi richiesti.

    :param yaml_file: Percorso del file YAML
    :raise IRValidatorException: quando mancano dati obbligatori nel file
    :return: Dizionario con i dati caricati da un file YAML
    """
    if yaml_file is None:
        raise IRValidatorException("Il percorso del file YAML non è stato fornito.")
    
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        raise IRValidatorException(f"File YAML non trovato: {yaml_file}")
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Errore nel parsing del file YAML: {e}")
    
    required_fields = ['field1', 'field2', 'field3']  # Esempio di campi obbligatori
    for field in required_fields:
        if field not in data:
            raise IRValidatorException(f"Campo obbligatorio mancante: {field}")
    
    return data