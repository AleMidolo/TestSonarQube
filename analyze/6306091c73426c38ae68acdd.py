import yaml

class IRValidatorException(Exception):
    pass

def validate_from_file(cls, yaml_file=None):
    required_fields = ['field1', 'field2', 'field3']  # Example required fields
    if yaml_file is None:
        raise ValueError("YAML file path must be provided.")
    
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Missing mandatory fields: {', '.join(missing_fields)}")
    
    return data