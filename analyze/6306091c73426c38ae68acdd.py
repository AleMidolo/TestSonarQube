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
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML file: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {yaml_file}")
    
    # Assuming required_fields is a class attribute or defined elsewhere
    required_fields = getattr(cls, 'required_fields', [])
    
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        raise IRValidatorException(f"Missing mandatory fields: {missing_fields}")
    
    return data