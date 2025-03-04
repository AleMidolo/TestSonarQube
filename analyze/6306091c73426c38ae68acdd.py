def validate_from_file(cls, yaml_file=None):
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file 
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    import yaml
    import os.path

    if yaml_file is None or not os.path.isfile(yaml_file):
        raise IRValidatorException(f"YAML file not found: {yaml_file}")

    try:
        with open(yaml_file, 'r') as f:
            yaml_data = yaml.safe_load(f)
            
        if not isinstance(yaml_data, dict):
            raise IRValidatorException("YAML file must contain a dictionary/mapping")
            
        # Validate required fields
        required_fields = ['name', 'description', 'version']
        missing_fields = [field for field in required_fields if field not in yaml_data]
        
        if missing_fields:
            raise IRValidatorException(f"Missing mandatory fields in YAML: {', '.join(missing_fields)}")
            
        return yaml_data
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error parsing YAML file: {str(e)}")
    except Exception as e:
        raise IRValidatorException(f"Unexpected error validating YAML file: {str(e)}")

class IRValidatorException(Exception):
    """Custom exception for YAML validation errors"""
    pass