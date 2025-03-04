def validate_from_content(cls, spec_content=None):
    """
    Valida che il contenuto dello spec (YAML) contenga tutti i campi richiesti.

    :param spec_content: contenuto del file spec
    :raise IRValidatorException: quando i dati obbligatori
    sono mancanti nel file spec
    :return: Dizionario con i dati caricati da un file spec (YAML)
    """
    if spec_content is None:
        raise IRValidatorException("Spec content cannot be None")
        
    required_fields = ['name', 'version', 'description']
    
    # Check if spec_content is a dictionary
    if not isinstance(spec_content, dict):
        raise IRValidatorException("Spec content must be a dictionary")
    
    # Validate required fields
    missing_fields = []
    for field in required_fields:
        if field not in spec_content:
            missing_fields.append(field)
            
    if missing_fields:
        raise IRValidatorException(
            f"Required fields missing in spec: {', '.join(missing_fields)}"
        )
            
    # Validate field types
    if not isinstance(spec_content.get('name'), str):
        raise IRValidatorException("'name' field must be a string")
        
    if not isinstance(spec_content.get('version'), (str, int, float)):
        raise IRValidatorException("'version' field must be a string, integer or float")
        
    if not isinstance(spec_content.get('description'), str):
        raise IRValidatorException("'description' field must be a string")
        
    return spec_content