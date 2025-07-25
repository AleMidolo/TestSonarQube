import yaml

class IRValidatorException(Exception):
    pass

def validate_from_file(cls, yaml_file=None):
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    if yaml_file is None:
        raise IRValidatorException("YAML file path is required.")

    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except Exception as e:
        raise IRValidatorException(f"Failed to load YAML file: {e}")

    # Example of mandatory fields validation
    mandatory_fields = ['field1', 'field2', 'field3']  # Replace with actual mandatory fields
    for field in mandatory_fields:
        if field not in data:
            raise IRValidatorException(f"Missing mandatory field: {field}")

    return data