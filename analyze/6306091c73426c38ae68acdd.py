import yaml

def validate_from_file(cls, yaml_file=None):
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    if yaml_file is None:
        raise ValueError("YAML file path must be provided.")
    
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except Exception as e:
        raise cls.IRValidatorException(f"Failed to load YAML file: {e}")
    
    # Assuming required_fields is a class attribute or method
    required_fields = cls.get_required_fields() if hasattr(cls, 'get_required_fields') else []
    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise cls.IRValidatorException(f"Missing mandatory fields: {', '.join(missing_fields)}")
    
    return data