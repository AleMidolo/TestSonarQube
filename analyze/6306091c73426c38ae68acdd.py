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
        raise IRValidatorException("No YAML file provided.")

    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except Exception as e:
        raise IRValidatorException(f"Error loading YAML file: {e}")

    required_fields = ['field1', 'field2', 'field3']  # Example required fields
    for field in required_fields:
        if field not in data:
            raise IRValidatorException(f"Missing required field: {field}")

    return data