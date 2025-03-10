import yaml

class IRValidatorException(Exception):
    pass

def validate_from_content(cls, spec_content=None):
    """
    Validates that spec (YAML) content has all required fields.

    :param spec_content: content of spec file
    :raise IRValidatorException: when mandatory data is missing in spec file
    :return: Dictionary with data loaded from a spec (YAML) file
    """
    if spec_content is None:
        raise IRValidatorException("Spec content cannot be None.")
    
    try:
        spec_data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Invalid YAML content: {e}")
    
    required_fields = ['field1', 'field2', 'field3']  # Example required fields
    
    for field in required_fields:
        if field not in spec_data:
            raise IRValidatorException(f"Missing mandatory field: {field}")
    
    return spec_data