def validate_from_content(cls, spec_content=None):
    """
    Valida che il contenuto dello spec (YAML) contenga tutti i campi richiesti.

    :param spec_content: contenuto del file spec
    :raise IRValidatorException: quando i dati obbligatori
    sono mancanti nel file spec
    :return: Dizionario con i dati caricati da un file spec (YAML)
    """
    import yaml

    required_fields = ['field1', 'field2', 'field3']  # Example required fields
    if spec_content is None:
        raise IRValidatorException("Spec content cannot be None")

    try:
        data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error parsing YAML: {e}")

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Missing required fields: {', '.join(missing_fields)}")

    return data