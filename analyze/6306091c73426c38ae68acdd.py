def validate_from_file(cls, yaml_file=None):
    """
    Carica e valida che un file YAML contenga tutti i campi richiesti.

    :param yaml_file: Percorso del file YAML
    :raise IRValidatorException: quando mancano dati obbligatori nel file
    :return: Dizionario con i dati caricati da un file YAML
    """
    import yaml

    required_fields = cls.get_required_fields()  # Assuming this method exists in the class
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f'Missing required fields: {", ".join(missing_fields)}')

    return data