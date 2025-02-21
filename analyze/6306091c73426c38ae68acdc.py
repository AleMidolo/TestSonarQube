def validate_from_content(cls, spec_content=None):
    """
    Valida che il contenuto dello spec (YAML) contenga tutti i campi richiesti.

    :param spec_content: contenuto del file spec
    :raise IRValidatorException: quando i dati obbligatori
    sono mancanti nel file spec
    :return: Dizionario con i dati caricati da un file spec (YAML)
    """
    import yaml

    required_fields = ['field1', 'field2', 'field3']  # Esempio di campi richiesti
    if spec_content is None:
        raise IRValidatorException("Il contenuto dello spec non può essere nullo.")

    try:
        data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Errore nel caricamento del file YAML: {e}")

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Campi obbligatori mancanti: {', '.join(missing_fields)}")

    return data