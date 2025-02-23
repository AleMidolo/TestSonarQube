def validate_from_file(cls, yaml_file=None):
    """
    Carica e valida che un file YAML contenga tutti i campi richiesti.

    :param yaml_file: Percorso del file YAML
    :raise IRValidatorException: quando mancano dati obbligatori nel file
    :return: Dizionario con i dati caricati da un file YAML
    """
    import yaml
    from pathlib import Path

    required_fields = cls.get_required_fields()  # Assuming this method exists in the class

    if yaml_file is None:
        raise ValueError("Il percorso del file YAML non può essere None.")

    yaml_path = Path(yaml_file)
    if not yaml_path.is_file():
        raise FileNotFoundError(f"Il file {yaml_file} non esiste.")

    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Mancano i seguenti campi obbligatori: {', '.join(missing_fields)}")

    return data